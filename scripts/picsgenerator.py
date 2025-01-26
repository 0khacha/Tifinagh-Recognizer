from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os

# Define the output directory
output_dir = "data/Tifinagh-MNIST/3"
os.makedirs(output_dir, exist_ok=True)

# Define the image size
image_size = (28, 28)  # 28x20 pixels

# Define the number of variations to generate
num_variations = 20

# Define a function to add randomness to the strokes
def add_randomness(draw, x, y, stroke_width):
    # Add some random noise to the position and stroke width
    x_noise = np.random.randint(-1, 2)  # Small horizontal variation
    y_noise = np.random.randint(-1, 2)  # Small vertical variation
    stroke_noise = np.random.randint(-1, 2)  # Small stroke width variation
    return x + x_noise, y + y_noise, stroke_width + stroke_noise

# Define a function to generate hand-drawn variations of a character
def generate_hand_drawn_variations(character, output_dir, num_variations):
    for i in range(num_variations):
        # Create a blank image with a white background
        image = Image.new("L", image_size, "white")
        draw = ImageDraw.Draw(image)

        # Define the font (you may need to install a Tifinagh font)
        try:
            font = ImageFont.truetype("arial.ttf", 18)  # Smaller font size for 28x20 image
        except IOError:
            font = ImageFont.load_default()  # Fallback to default font

        # Draw the character with some randomness
        x, y = 5, 2  # Starting position (adjusted for 28x20 size)
        stroke_width = 1  # Base stroke width

        # Draw the character multiple times with slight variations
        for _ in range(3):  # Draw the character 3 times with randomness
            x_new, y_new, stroke_new = add_randomness(draw, x, y, stroke_width)
            draw.text((x_new, y_new), character, font=font, fill="black")

        # Save the image
        output_path = os.path.join(output_dir, f"{character}_variation_{i + 1}.png")
        image.save(output_path)
        print(f"Saved: {output_path}")

# Input the character from the user
character = input("Enter the Tifinagh character: ")

# Generate 20 hand-drawn variations of the character
generate_hand_drawn_variations(character, output_dir, num_variations)

print(f"Generated {num_variations} hand-drawn variations of '{character}' in '{output_dir}'.")