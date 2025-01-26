from PIL import Image
import os

# Define the directory containing the images
input_dir = r'C:\Users\THINKUP\Desktop\Tifinagh_CNN\data\AMHCD_64\yarr'  # Use raw string
output_dir = r'C:\Users\THINKUP\Desktop\Tifinagh_CNN\data\Tifinagh-MNIST\32'  # Use raw string

# Debugging: Print paths
print(f"Input directory: {input_dir}")
print(f"Output directory: {output_dir}")

# Check if input directory exists
if not os.path.exists(input_dir):
    print(f"Input directory does not exist: {input_dir}")
    exit()

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Created output directory: {output_dir}")

# Desired size
size = (28, 28)

# Debugging: List files in input directory
print(f"Files in input directory: {os.listdir(input_dir)}")

# Loop through all files in the input directory
for filename in os.listdir(input_dir):
    # Check if the file is an image
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        # Open the image
        img_path = os.path.join(input_dir, filename)
        with Image.open(img_path) as img:
            # Resize the image
            resized_img = img.resize(size, Image.Resampling.LANCZOS)  # Updated line
            
            # Save the resized image to the output directory
            output_path = os.path.join(output_dir, filename)
            resized_img.save(output_path)
            print(f"Resized and saved: {output_path}")
    else:
        print(f"Skipping non-image file: {filename}")

print("All images have been resized and saved.")