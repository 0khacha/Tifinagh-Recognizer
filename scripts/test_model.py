import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# Define the Tifinagh characters and their French meanings
characters = {
    '0': ('ⴰ', 'a'),    # Folder 0 contains images of "ⴰ" (a)
    '1': ('ⴱ', 'b'),    # Folder 1 contains images of "ⴱ" (b)
    '2': ('ⵛ', 'ch'),   # Folder 2 contains images of "ⵛ" (ch)
    '3': ('ⴷ', 'd'),    # Folder 3 contains images of "ⴷ" (d)
    '4': ('ⴻ', 'e'),    # Folder 4 contains images of "ⴻ" (e)
    '5': ('ⴼ', 'f'),    # Folder 5 contains images of "ⴼ" (f)
    '6': ('ⴳ', 'g'),    # Folder 6 contains images of "ⴳ" (g)
    '7': ('ⵀ', 'h'),    # Folder 7 contains images of "ⵀ" (h)
    '8': ('ⵉ', 'i'),    # Folder 8 contains images of "ⵉ" (i)
    '9': ('ⵊ', 'j'),    # Folder 9 contains images of "ⵊ" (j)
    '10': ('ⴽ', 'k'),   # Folder 10 contains images of "ⴽ" (k)
    '11': ('ⵍ', 'l'),   # Folder 11 contains images of "ⵍ" (l)
    '12': ('ⵎ', 'm'),   # Folder 12 contains images of "ⵎ" (m)
    '13': ('ⵏ', 'n'),   # Folder 13 contains images of "ⵏ" (n)
    '14': ('ⵇ', 'q'),   # Folder 14 contains images of "ⵇ" (q)
    '15': ('ⵔ', 'r'),   # Folder 15 contains images of "ⵔ" (r)
    '16': ('ⵙ', 's'),   # Folder 16 contains images of "ⵙ" (s)
    '17': ('ⵜ', 't'),   # Folder 17 contains images of "ⵜ" (t)
    '18': ('ⵓ', 'u'),   # Folder 18 contains images of "ⵓ" (u)
    '19': ('ⵡ', 'w'),   # Folder 19 contains images of "ⵡ" (w)
    '20': ('ⵅ', 'kh'),  # Folder 20 contains images of "ⵅ" (kh)
    '21': ('ⵢ', 'y'),   # Folder 21 contains images of "ⵢ" (y)
    '22': ('ⵣ', 'z'),   # Folder 22 contains images of "ⵣ" (z)
    '23': ('ⵃ', 'ḥ'),   # Folder 23 contains images of "ⵃ" (ḥ)
    '24': ('ⵚ', 'ṣ'),   # Folder 24 contains images of "ⵚ" (ṣ)
    '25': ('ⴹ', 'ḍ'),   # Folder 25 contains images of "ⴹ" (ḍ)
    '26': ('ⵟ', 'ṭ'),   # Folder 26 contains images of "ⵟ" (ṭ)
    '27': ('ⵄ', 'ɛ'),   # Folder 27 contains images of "ⵄ" (ɛ)
    '28': ('ⵖ', 'ɣ'),   # Folder 28 contains images of "ⵖ" (ɣ)
    '29': ('ⵥ', 'ẓ'),   # Folder 29 contains images of "ⵥ" (ẓ)
    '30': ('ⴳⵯ', 'gw'), # Folder 30 contains images of "ⴳⵯ" (gw)
    '31': ('ⴽⵯ', 'kw'), # Folder 31 contains images of "ⴽⵯ" (kw)
    '32': ('ⵕ', 'ṛ')    # Folder 32 contains images of "ⵕ" (ṛ)
}

# Load the saved model
model = tf.keras.models.load_model('tifinagh_char_classifier.h5')

# Function to test the model with an example image
def test_model_with_example(image_path):
    # Load and preprocess the test image
    img = image.load_img(image_path, target_size=(28, 28), color_mode='grayscale')
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Rescale the image

    # Make a prediction
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)[0]

    # Map the predicted class index to the corresponding Tifinagh character
    if str(predicted_class) in characters:
        predicted_character = characters[str(predicted_class)]
        print(f'Predicted character: {predicted_character[0]} ({predicted_character[1]})')
    else:
        print(f'Error: Predicted class index {predicted_class} is out of range.')

# Example usage: Test the model with an image
test_image_path = "Tifinagh-MNIST\00\0.png"  # Replace with the path to your test image
test_model_with_example(test_image_path)