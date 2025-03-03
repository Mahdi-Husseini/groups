import streamlit as st
import os
from PIL import Image

st.title('Efficient Frontier of All Groups')

# Get the directory where the Python script is located
script_directory = os.path.dirname(os.path.abspath(__file__))


# Define the desired image size (optional)
IMAGE_SIZE = (300, 300)  # Adjust as needed

# Get all PNG files in the directory
png_files = [file for file in os.listdir(script_directory) if file.lower().endswith(".png")]

# Sort the list of images (optional)
png_files.sort()

# Display images in pairs (2 per row)
for i in range(0, len(png_files), 2):  # Step through images in pairs
    cols = st.columns(2)  # Create two columns
    
    for j in range(2):  # Place two images per row
        if i + j < len(png_files):  # Check if there's an image to display
            file_path = os.path.join(script_directory, png_files[i + j])
            img = Image.open(file_path).resize(IMAGE_SIZE)  # Resize image
            
            # Display image in corresponding column
            cols[j].image(img, caption=png_files[i + j], use_container_width=True)
