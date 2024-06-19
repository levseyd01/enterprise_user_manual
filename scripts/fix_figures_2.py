import re
import os
import sys
# List of image file names


# Read the content of the file
with open("index_Copy.rst", "r", encoding="utf-8") as file:
    content = file.read()

# Initialize the image file index
image_index = 0

# Define the regular expression pattern to match the image placeholders
pattern = r"page_\d+_image_\d+\.png"

# Function to replace the image placeholders
def replace_image_placeholder(match):
    global image_index
    if image_index < len(image_files):
        replacement = image_files[image_index]
        image_index += 1
        return replacement
    return match.group()

# Replace the image placeholders in the content
updated_content = re.sub(pattern, replace_image_placeholder, content)
# Replace each placeholder image file name with the corresponding image file nam
# e
for i, image_file in enumerate(image_files):
    placeholder = f"page_{i+8}_image_\\d+\\.png"
    content = re.sub(placeholder, image_file, content, count=1)
    print ("content", content)
# Write the updated content back to the file
# Write the updated content back to the file
with open("index_Copy.rst", "w", encoding="utf-8") as file:
    file.write(content)