import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.colorchooser import askcolor
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image, ImageTk, ImageOps, ImageDraw
import os

# Define the base directory and model path
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Root directory (TIFINAGH_CNN)
model_path = os.path.join(base_dir, "models", "tifinagh_model342.h5")

# Create a folder for temporary images if it doesn't exist
temp_image_folder = os.path.join(base_dir, "tests")
os.makedirs(temp_image_folder, exist_ok=True)

# Load the model
model = load_model(model_path)
print("Model loaded successfully!")

# Define the Tifinagh characters and their French meanings
characters = {
    0: ('ⴰ', 'a'),    1: ('ⴱ', 'b'),    2: ('ⵛ', 'ch'),
    3: ('ⴷ', 'd'),    4: ('ⴻ', 'e'),    5: ('ⴼ', 'f'),
    6: ('ⴳ', 'g'),    7: ('ⵀ', 'h'),    8: ('ⵉ', 'i'),
    9: ('ⵊ', 'j'),    10: ('ⴽ', 'k'),   11: ('ⵍ', 'l'),
    12: ('ⵎ', 'm'),   13: ('ⵏ', 'n'),   14: ('ⵇ', 'q'),
    15: ('ⵔ', 'r'),   16: ('ⵙ', 's'),   17: ('ⵜ', 't'),
    18: ('ⵓ', 'u'),   19: ('ⵡ', 'w'),   20: ('ⵅ', 'kh'),
    21: ('ⵢ', 'y'),   22: ('ⵣ', 'z'),   23: ('ⵃ', 'ḥ'),
    24: ('ⵚ', 'ṣ'),   25: ('ⴹ', 'ḍ'),   26: ('ⵟ', 'ṭ'),
    27: ('ⵄ', 'ɛ'),   28: ('ⵖ', 'ɣ'),   29: ('ⵥ', 'ẓ'),
    30: ('ⴳⵯ', 'gw'), 31: ('ⴽⵯ', 'kw'), 32: ('ⵕ', 'ṛ')
}

def preprocess_image(image):
    # Resize to 64x64 (matching the model's expected input shape)
    image = image.resize((64, 64))
    # Convert to grayscale
    image = image.convert("L")
    # Invert colors (black background, white strokes)
    image = ImageOps.invert(image)
    
    # Apply a binary threshold to make the image strictly black and white
    threshold = 127  # Adjust this value if needed
    image = image.point(lambda p: 255 if p > threshold else 0)
    
    # Convert to numpy array
    image = np.array(image)
    # Normalize to [0, 1]
    image = image.astype('float32') / 255.0
    # Add channel dimension
    image = np.expand_dims(image, axis=-1)
    # Add batch dimension
    image = np.expand_dims(image, axis=0)
    return image

def predict_character(image):
    prediction = model.predict(image)
    predicted_class = np.argmax(prediction, axis=1)[0]
    confidence = np.max(prediction) * 100  # Confidence percentage
    tifinagh_char, french_meaning = characters.get(predicted_class, ('Unknown', 'Unknown'))
    return tifinagh_char, french_meaning, confidence

def upload_image():
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )
    if file_path:
        try:
            image = Image.open(file_path)
            try:
                resampling_method = Image.Resampling.LANCZOS
            except AttributeError:
                resampling_method = Image.ANTIALIAS
            image = image.resize((200, 200), resampling_method)
            photo = ImageTk.PhotoImage(image)
            image_label.config(image=photo)
            image_label.image = photo

            # Preprocess and predict
            processed_image = preprocess_image(Image.open(file_path))
            tifinagh_char, french_meaning, confidence = predict_character(processed_image)
            result_label.config(
                text=f"Predicted Character: {tifinagh_char}\nFrench Meaning: {french_meaning}\nConfidence: {confidence:.2f}%",
                fg="#4CAF50"  # Green color
            )
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process the image: {e}")

def predict_drawing():
    # Create a blank image with the same size as the canvas
    img = Image.new("RGB", (canvas.winfo_width(), canvas.winfo_height()), "white")
    draw = ImageDraw.Draw(img)

    # Get all drawn items from the canvas
    for item in canvas.find_all():
        # Get the coordinates of the item
        coords = canvas.coords(item)
        # Get the color of the item
        color = canvas.itemcget(item, "fill")
        # Draw the item on the Pillow image
        if canvas.type(item) == "oval":
            draw.ellipse(coords, fill=color, outline=color)
        elif canvas.type(item) == "line":
            draw.line(coords, fill=color, width=int(canvas.itemcget(item, "width")))

    # Save the drawn image temporarily
    temp_image_path = os.path.join(temp_image_folder, "drawing.png")
    img.save(temp_image_path)

    # Preprocess and predict
    processed_image = preprocess_image(img)
    tifinagh_char, french_meaning, confidence = predict_character(processed_image)
    result_label.config(
        text=f"Predicted Character: {tifinagh_char}\nFrench Meaning: {french_meaning}\nConfidence: {confidence:.2f}%",
        fg="#4CAF50"  # Green color
    )

def clear_canvas():
    canvas.delete("all")
    result_label.config(text="")

def paint(event):
    stroke_width = int(brush_size.get())
    x1, y1 = (event.x - stroke_width), (event.y - stroke_width)
    x2, y2 = (event.x + stroke_width), (event.y + stroke_width)
    canvas.create_oval(x1, y1, x2, y2, fill=current_color, outline=current_color, width=stroke_width)

def change_color():
    global current_color
    color = askcolor(color=current_color)[1]
    if color:
        current_color = color

def open_drawing_window():
    global drawing_window, canvas, brush_size, current_color
    drawing_window = tk.Toplevel(root)
    drawing_window.title("Draw Tifinagh Character")
    drawing_window.geometry("450x350")  # Adjusted height to fit buttons
    drawing_window.configure(bg="#f0f0f0")

    # Create a canvas for drawing
    canvas = tk.Canvas(drawing_window, bg="white", width=250, height=250)
    canvas.pack(pady=10)

    # Bind mouse events to draw on the canvas
    canvas.bind("<B1-Motion>", paint)

    # Create a frame for buttons
    drawing_button_frame = tk.Frame(drawing_window, bg="#f0f0f0")
    drawing_button_frame.pack(pady=10)

    # Create a button to predict the drawing
    predict_button = ttk.Button(
        drawing_button_frame,
        text="Predict",
        command=predict_drawing,
        style="TButton"
    )
    predict_button.pack(side=tk.LEFT, padx=10)

    # Create a button to clear the canvas
    clear_button = ttk.Button(
        drawing_button_frame,
        text="Clear",
        command=clear_canvas,
        style="TButton"
    )
    clear_button.pack(side=tk.LEFT, padx=10)

    # Create a button to change brush color
    color_button = ttk.Button(
        drawing_button_frame,
        text="Change Color",
        command=change_color,
        style="TButton"
    )
    color_button.pack(side=tk.LEFT, padx=10)

    # Create a slider for brush size
    brush_size = tk.Scale(drawing_button_frame, from_=1, to=20, orient=tk.HORIZONTAL, label="Brush Size")
    brush_size.set(8)
    brush_size.pack(side=tk.LEFT, padx=10)

    # Set default color
    current_color = "black"

# Create the main window
root = tk.Tk()
root.title("Tifinagh Character Recognition")
root.geometry("600x600")
root.configure(bg="#f0f0f0")  # Light gray background

# Custom font
custom_font = ("Helvetica", 12)

# Create a label for the title
title_label = tk.Label(
    root,
    text="Tifinagh Character Recognition",
    font=("Helvetica", 18, "bold"),
    fg="#333333",  # Dark gray color
    bg="#f0f0f0"
)
title_label.pack(pady=20)

# Create a frame for the buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

# Create a button to upload an image
upload_button = ttk.Button(
    button_frame,
    text="Upload Image",
    command=upload_image,
    style="TButton"
)
upload_button.pack(side=tk.LEFT, padx=10)

# Create a button to draw and predict
draw_button = ttk.Button(
    button_frame,
    text="Draw Character",
    command=lambda: open_drawing_window(),
    style="TButton"
)
draw_button.pack(side=tk.LEFT, padx=10)

# Create a label to display the uploaded image
image_label = tk.Label(root, bg="#f0f0f0")
image_label.pack(pady=20)

# Create a label to display the prediction result
result_label = tk.Label(
    root,
    text="",
    font=custom_font,
    fg="#4CAF50",  # Green color
    bg="#f0f0f0"
)
result_label.pack(pady=10)

# Create a footer label
footer_label = tk.Label(
    root,
    text="Developed by 0khacha",
    font=("Helvetica", 10),
    fg="#777777",  # Light gray color
    bg="#f0f0f0"
)
footer_label.pack(side=tk.BOTTOM, pady=10)

# Run the Tkinter event loop
root.mainloop()