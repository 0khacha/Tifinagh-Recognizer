import os
import cv2
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical

# Load the dataset metadata
csv_file_path = 'metadatatifinagh_dataset.csv'
data = pd.read_csv(csv_file_path)

# Initialize lists to store images and labels
images = []
labels = []

# Load and preprocess images
for index, row in data.iterrows():
    image_path = row['image_path']
    label = row['folder']  # Use folder as the label (e.g., 00, 01, etc.)
    
    # Check if the image file exists
    if not os.path.exists(image_path):
        print(f"Image not found: {image_path}")
        continue  # Skip this image
    
    # Read the image
    try:
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Read as grayscale
        
        # Check if the image was loaded successfully
        if image is None:
            print(f"Failed to load image: {image_path}")
            continue  # Skip this image
        
        # Resize the image
        image = cv2.resize(image, (64, 64))  # Resize to 64x64
        
        # Normalize the image
        image = image.astype('float32') / 255.0  # Normalize to [0, 1]
        
        # Append to lists
        images.append(image)
        labels.append(int(label))  # Convert folder name to integer label
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        continue  # Skip this image

# Check if any images were loaded
if not images:
    raise ValueError("No images were loaded. Check the dataset paths and files.")

# Convert lists to numpy arrays
images = np.array(images)
labels = np.array(labels)

# One-hot encode the labels
num_classes = len(data['folder'].unique())
labels = to_categorical(labels, num_classes=num_classes)

# Split the dataset into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(images, labels, test_size=0.2, random_state=42)

# Build the model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(num_classes, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Print the model summary
model.summary()

# Train the model
history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=20,
    batch_size=32
)

# Save the trained model
model.save('tifinagh_model_vf.h5')
print("Model saved as tifinagh_modelvf.h5")