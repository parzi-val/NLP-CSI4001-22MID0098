import streamlit as st
import os
from PIL import Image

# Set directory where word clouds are stored
wordcloud_dir = "wordclouds"

st.set_page_config(layout="wide")   

# Ensure directory exists
if not os.path.exists(wordcloud_dir):
    st.error(f"Directory '{wordcloud_dir}' not found! Please generate word clouds first.")
else:
    st.title("Presidential Inaugural Addresses - Word Cloud Gallery")

    # Get all word cloud images
    images = [img for img in os.listdir(wordcloud_dir) if img.endswith(".png")]

    if not images:
        st.warning("No word clouds found! Generate them first.")
    else:
        # Sort images by year (assuming filenames are like '1789-Washington_wordcloud.png')
        images.sort()

        # Display images in a grid
        cols = st.columns(4)  # 3 images per row
        for idx, image in enumerate(images):
            img_path = os.path.join(wordcloud_dir, image)
            img = Image.open(img_path)
            
            # Display image with its filename as caption
            with cols[idx % 4]:  # Place in respective column
                st.image(img, caption=image, use_container_width=True)
