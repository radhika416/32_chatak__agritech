import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import matplotlib.pyplot as plt

# Load the pre-trained FCN model
model_path = "/content/disease_detection_model.h5"

# Verify file size before loading
file_size = os.path.getsize(model_path)
print(f"File size of disease_detection_model.h5: {file_size} bytes")
# Compare this size to the expected size of the model file. 
# If it's smaller, re-download or re-save the model.

# Load the model after verifying file integrity
model = load_model(model_path)

# Load and preprocess the input image
def preprocess_image(image_path, target_size):
    image = Image.open(image_path).convert("RGB")
    image = image.resize(target_size)
    image_array = np.array(image) / 255.0  # Normalize pixel values
    return image_array, image

# Replace with the actual path to your input image
input_image_path = "/content/image.jpg"  # Example: If your image is in the Colab content folder
#input_image_path = "/path/to/your/image.jpg"  # Or provide the full path to your image

input_size = (224, 224)  # Resize to model input size
image_array, original_image = preprocess_image(input_image_path, input_size)

# Perform prediction
image_batch = np.expand_dims(image_array, axis=0)  # Add batch dimension
prediction = model.predict(image_batch)

# Check the shape of the prediction
print("Shape of prediction:", prediction.shape) 

# Reshape or process the prediction if necessary
# This will depend on the model's output. 
# If the model is intended for segmentation, it should output a 
# 2D or 3D array representing the segmentation mask.
# For example, if the model outputs a 1D array of class probabilities,
# you'll need to reshape it based on your desired segmentation output shape.

# Assuming a segmentation model with output shape (1, 224, 224, 1)
# where the last dimension represents the class (e.g., 0 for background, 1 for infected area)

# Reshape the prediction for binary segmentation (adjust based on your model's output)
# segmentation_mask = prediction.reshape(input_size) 
# OR:
# Reshape the prediction for multi-class segmentation 
# segmentation_mask = np.argmax(prediction, axis=-1).reshape(input_size) # Example for one-hot encoded output

# Then continue with the rest of the script...

# Placeholder - Replace with appropriate reshaping/processing based on model's output
segmentation_mask = prediction.squeeze() # Previous line causing the issue

# Threshold the segmentation mask
threshold = 0.5
binary_mask = (segmentation_mask > threshold).astype(np.uint8)

# Calculate infection percentage
infection_pixels = np.sum(binary_mask)
total_pixels = binary_mask.size
infection_percentage = (infection_pixels / total_pixels) * 100

print(f"Infection extent: {infection_percentage:.2f}%")

# Display results
plt.figure(figsize=(12, 6))
plt