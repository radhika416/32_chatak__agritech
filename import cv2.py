import cv2
import numpy as np
import matplotlib.pyplot as plt

def detect_disease_in_leaf(image_path):
    # Load the image
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Convert to HSV for better color segmentation
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Refined HSV range for green areas (healthy leaf parts)
    lower_green = np.array([35, 50, 50])  # Adjusted lower bound of green in HSV
    upper_green = np.array([85, 255, 255])  # Adjusted upper bound of green in HSV

    # Create a mask for green regions
    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    # Create a mask for non-green regions (diseased areas)
    diseased_mask = cv2.bitwise_not(green_mask)  # Invert the green mask to get diseased regions

    # Optional: Apply morphological operations to remove noise and refine the masks
    kernel = np.ones((5, 5), np.uint8)
    diseased_mask_cleaned = cv2.morphologyEx(diseased_mask, cv2.MORPH_CLOSE, kernel)

    # Apply the mask to the original image to highlight diseased areas
    diseased_region = cv2.bitwise_and(image_rgb, image_rgb, mask=diseased_mask_cleaned)

    return diseased_region, diseased_mask_cleaned, green_mask

def calculate_disease_percentage(diseased_mask, green_mask):
    # Calculate total leaf area (green + non-green pixels)
    total_leaf_area = cv2.countNonZero(diseased_mask) + cv2.countNonZero(green_mask)

    # Calculate diseased area (non-green pixels)
    diseased_area = cv2.countNonZero(diseased_mask)
    nondiseased_area = cv2.countNonZero(green_mask)

    # Percentage of diseased area
    disease_percentage = (nondiseased_area / total_leaf_area) * 100
    return disease_percentage

def visualize_disease_detection(image_path):
    diseased_region, diseased_mask, green_mask = detect_disease_in_leaf(image_path)

    # Calculate disease percentage
    disease_percentage = calculate_disease_percentage(diseased_mask, green_mask)
    return disease_percentage

  

# Save the uploaded image and process it

def main(image_path):
  uploaded_image_path = image_path  # Path to the uploaded image
  return visualize_disease_detection(uploaded_image_path)
if __name__ == "__main__":
    print(main())