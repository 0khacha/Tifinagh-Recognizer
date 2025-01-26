import os

# Root folder
root_folder = 'tifinaghdataset'

# List of Tifinagh characters
tifinagh_chars = [
    'a', 'aa', 'b', 'ch', 'd', 'dd', 'e', 'f', 'g',
    'gh', 'h', 'hh', 'i', 'j', 'k', 'kh', 'l', 'm',
    'n', 'q', 'r', 's', 'ss', 't', 'tt', 'u', 'w',
    'ww', 'y', 'z', 'zz'
]

# Create folders and placeholder images
for folder_num in range(44):  # Folders 00 to 43
    folder_name = f"{folder_num:02d}"  # Format as 00, 01, ..., 43
    folder_path = os.path.join(root_folder, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    
    for char in tifinagh_chars:
        if folder_num == 0:
            image_name = f"{char}.png"  # For folder 00: a.png, aa.png, b.png, etc.
        else:
            image_name = f"{char}{folder_num}.png"  # For folders 01-43: a1.png, aa1.png, b1.png, etc.
        
        image_path = os.path.join(folder_path, image_name)
        
        # Create a placeholder image (you can replace this with actual images later)
        with open(image_path, 'w') as f:
            f.write("")  # Creates an empty file

print("Folder structure and placeholder images created successfully!")