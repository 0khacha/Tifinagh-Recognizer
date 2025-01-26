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

# List of Tifinagh characters from the first dataset
tifinagh_chars = [
    'a', 'aa', 'b', 'ch', 'd', 'dd', 'e', 'f', 'g',
    'gh', 'h', 'hh', 'i', 'j', 'k', 'kh', 'l', 'm',
    'n', 'q', 'r', 's', 'ss', 't', 'tt', 'u', 'w',
    'ww', 'y', 'z', 'zz'
]

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the paths to the dataset directories
dataset_dirs = [
    os.path.join(script_dir, '..', 'data', 'tifinaghdataset'),
    os.path.join(script_dir, '..', 'data', 'Tifinagh-MNIST')
]

# Supported image file extensions
image_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp']

# Create a CSV file to store the dataset information
csv_file_path = os.path.join(script_dir, 'metadatatifinagh_dataset4.csv')

# Counters for processed and not processed images
processed_images = 0
not_processed_images = 0

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['folder', 'filename', 'tifinagh_char', 'french_meaning', 'image_path'])

    # Iterate over each dataset directory
    for dataset_dir in dataset_dirs:
        # Get the folder name (e.g., 'tifinaghdataset' or 'Tifinagh-MNIST')
        dataset_name = os.path.basename(dataset_dir)
        
        # Iterate over each folder in the dataset directory
        for folder_name in os.listdir(dataset_dir):
            folder_path = os.path.join(dataset_dir, folder_name)
            
            # Debug: Print the folder being processed
            print(f"Processing folder: {folder_name} in {dataset_dir}")
            
            # Check if it's a directory
            if os.path.isdir(folder_path):
                # Handle the tifinaghdataset folder (placeholder images)
                if dataset_name == 'tifinaghdataset':
                    try:
                        folder_num = int(folder_name)  # Folder names are numbers (00, 01, etc.)
                        if str(folder_num) in characters:
                            char, french_meaning = characters[str(folder_num)]
                            
                            # Iterate over each placeholder image in the folder
                            for char_name in tifinagh_chars:
                                # Check for both .png and .jpg extensions
                                for ext in ['.png', '.jpg']:
                                    if folder_num == 0:
                                        image_name = f"{char_name}{ext}"  # For folder 00: a.png, a.jpg, etc.
                                    else:
                                        image_name = f"{char_name}{folder_num}{ext}"  # For folders 01-43: a1.png, a1.jpg, etc.
                                    
                                    image_path = os.path.join(folder_path, image_name)
                                    
                                    # Check if the image exists
                                    if os.path.exists(image_path):
                                        # Get the relative path (relative to the data folder)
                                        relative_path = os.path.relpath(image_path, start=os.path.join(script_dir, '..', 'data'))
                                        
                                        # Write the folder name, filename, Tifinagh character, French meaning, and relative image path to the CSV
                                        writer.writerow([folder_name, image_name, char, french_meaning, relative_path])
                                        processed_images += 1  # Increment processed counter
                                        break  # Stop checking other extensions if the image is found
                                else:
                                    # If no image is found for the current character, increment the not processed counter
                                    print(f"Image not found: {image_path}")
                                    not_processed_images += 1
                    except ValueError:
                        print(f"Skipping invalid folder: {folder_name}")
                        not_processed_images += 1  # Increment not processed counter
                
                # Handle the Tifinagh-MNIST folder (actual images)
                elif dataset_name == 'Tifinagh-MNIST':
                    if folder_name in characters:
                        char, french_meaning = characters[folder_name]
                        
                        # Iterate over each file in the folder
                        for filename in os.listdir(folder_path):
                            # Check if the file is an image (based on extension)
                            if any(filename.lower().endswith(ext) for ext in image_extensions):
                                image_path = os.path.join(folder_path, filename)
                                
                                # Get the relative path (relative to the data folder)
                                relative_path = os.path.relpath(image_path, start=os.path.join(script_dir, '..', 'data'))
                                
                                # Write the folder name, filename, Tifinagh character, French meaning, and relative image path to the CSV
                                writer.writerow([folder_name, filename, char, french_meaning, relative_path])
                                processed_images += 1  # Increment processed counter
                            else:
                                not_processed_images += 1  # Increment not processed counter

# Print the results
print(f"Number of images processed: {processed_images}")
print(f"Number of images not processed: {not_processed_images}")
print(f"Dataset CSV created at {csv_file_path}")