import os
from datetime import datetime
import cv2
import numpy as np
import pandas as pd

# Import all functions directly from your module
from phenolopy import *

def process_images(images_folder):
    # Get a list of all image files in the folder
    image_files = [f for f in os.listdir(images_folder) if f.endswith('.jpg')]

    # Sort image files based on their names (assuming the names follow YYYY_MM_DD_HHMMSS.jpg format)
    image_files.sort()

    gcc_data = []

    for image_file in image_files:
        # Construct the full path to the image
        image_path = os.path.join(images_folder, image_file)

        # Extract date and time information from the filename
        date_str, time_str = image_file.split('_')[1:3]
        datetime_str = f"{date_str}_{time_str}"
        image_datetime = datetime.strptime(datetime_str, '%Y_%m_%d_%H%M%S')

        # Read the image
        image = cv2.imread(image_path)

        # Calculate GCC from the image
        gcc_value = calculate_gcc_from_image(image)

        # Append the results to the list
        gcc_data.append({
            'Image': image_file,
            'Date': image_datetime.date(),
            'Timestamp': image_datetime.time(),
            'GCC': gcc_value
        })

    # Create a DataFrame from the list of results
    df = pd.DataFrame(gcc_data)

    return df

if __name__ == "__main__":
    images_folder_path = './'

    # Call the function to process images and get the DataFrame
    gcc_dataframe = process_images(images_folder_path)

    # Print or use the resulting DataFrame as needed
    print(gcc_dataframe)
