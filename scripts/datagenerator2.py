import os
import csv

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

# Path to the dataset directory
dataset_dir = 'Tifinagh-MNIST'

# Create a CSV file to store the dataset information
csv_file_path = 'metadatatifinagh_dataset.csv'
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['folder', 'filename', 'tifinagh_char', 'french_meaning', 'image_path'])

    # Iterate over each folder in the dataset directory
    for folder_name in os.listdir(dataset_dir):
        folder_path = os.path.join(dataset_dir, folder_name)
        
        # Debug: Print the folder being processed
        print(f"Processing folder: {folder_name}")
        
        # Check if it's a directory and corresponds to a known Tifinagh character
        if os.path.isdir(folder_path) and folder_name in characters:
            char, french_meaning = characters[folder_name]
            
            # Debug: Print the Tifinagh character and French meaning
            print(f"  Tifinagh character: {char}, French meaning: {french_meaning}")
            
            # Iterate over each file in the folder
            for filename in os.listdir(folder_path):
                if filename.endswith('.png'):
                    # Construct the full image path
                    image_path = os.path.join(folder_path, filename)
                    
                    # Debug: Print the image being processed
                    print(f"    Processing image: {filename}")
                    
                    # Write the folder name, filename, Tifinagh character, French meaning, and image path to the CSV
                    writer.writerow([folder_name, filename, char, french_meaning, image_path])
        else:
            # Debug: Print if the folder is not recognized
            print(f"  Folder {folder_name} is not recognized or is not a directory.")

print(f"Dataset CSV created at {csv_file_path}")