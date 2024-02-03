import phencode
import numpy as np
import cv2
import os
from datetime import datetime

def calculate_gcc_from_image(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Extract the Green channel
    green_channel = hsv_image[:, :, 1]

    # Calculate the GCC
    gcc = np.mean(green_channel) / 255.0  # Normalize to range [0, 1]

    return gcc

def process_images(image_folder):
    # Get a list of all image files in the folder
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg')]

    # Sort image files based on their names (assuming the names follow YYYY_MM_DD_HHMMSS.jpg format)
    image_files.sort()

    for image_file in image_files:
        # Construct the full path to the image
        image_path = os.path.join(image_folder, image_file)

        # Extract date and time information from the filename
        date_str, time_str = image_file.split('_')[1:3]
        datetime_str = f"{date_str}_{time_str}"
        image_datetime = datetime.strptime(datetime_str, '%Y_%m_%d_%H%M%S')

        # Calculate GCC from the image
        gcc_value = calculate_gcc_from_image(image_path)

        # Print or save the results as needed
        print(f"Image: {image_file}, Date: {image_datetime}, GCC: {gcc_value}")

if __name__ == "__main__":
    image_folder_path = './'
    process_images(image_folder_path)
