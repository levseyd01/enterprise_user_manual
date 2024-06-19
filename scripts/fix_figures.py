import os
import re
import sys


# Get the absolute path to the directory containing the script

def list_files(directory, extension=None):
    """List all files in a directory with an optional extension filter."""
    print(f"Listing files in {directory}")
    if extension:
        files = [f for f in os.listdir(directory) if f.endswith(extension)]
    else:
        files = os.listdir(directory)
    return sorted(files, key=sort_key)  #

def find_pattern(rst_directory, images_directory):
    print(f"Updating RST files in {rst_directory} with images from {images_directory}")
    image_files = list_files(images_directory, '.png')
    print("image file found", image_files)

    for image_file in image_files:
        print(image_file)
    pattern = re.compile(r'(\.\. figure:: _static/pdf_images/)(page_\d+_image_\d+\.png)')

    for rst_file in list_files(rst_directory, '.rst'):
        rst_file_path = os.path.join(rst_directory, rst_file)
        with open(rst_file_path, 'r', encoding='utf-8') as file:
            print(f"Updating {rst_file_path}")

            content = file.readlines()

        updated_content = []
        print(f"Updating {rst_file_path}")
        for line in content:
            match = pattern.search(line)  # Search for the pattern in the line
            if match and image_files:  # Check if there's a match and we have image files left
                # Replace filename while keeping the prefix
                new_filename = image_files.pop(0)  # Get the first image filename and remove it from the list
                new_line = match.group(1) + new_filename + '\n'  # Construct new line
                updated_content.append(new_line)
            else:
                updated_content.append(line)

        with open(rst_file_path, 'w', encoding='utf-8') as file:

            file.writelines(updated_content)
            print(f"Updated {rst_file_path} with", updated_content)




def sort_key(filename):
    # This regex extracts 'page' and 'image' numbers from filenames like "page_10_image_1.png"
    match = re.search(r'page_(\d+)_image_(\d+)\.png', filename)
    if match:
        return (int(match.group(1)), int(match.group(2)))  # Return a tuple of integers for sorting
    return (0, 0)  # Default value for filenames that do not match the pattern


def update_rst_file(filepath, new_images_iter):
    print("updating rst file")
    pattern = re.compile(r'(\.\. figure:: _static/pdf_images/)(page_\d+_image_\d+\.png)')
    updated_content = []
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            match = pattern.search(line)
            if match:
                try:
                    new_image_name = next(new_images_iter)
                    print(f"old name is: {match}, updating to new name: {new_image_name}")# Get the next image name
                    new_line = f"{match.group(1)}{new_image_name}\n"  # Construct new line
                    updated_content.append(new_line)
                except StopIteration:
                    print("Ran out of new images to use for replacement.")
                    updated_content.append(line)  # Keep the line unchanged if no images left
            else:
                updated_content.append(line)

        with open(filepath, 'w', encoding='utf-8') as file:
            file.writelines(updated_content)

    except IOError as e:
        print(f"Error updating file {filepath}: {e}")


def main():
    print("starting main")
    directory_to_update = "to_update"
    print("image file found", directory_to_update)
    directory_with_new_images= "../source/_static/pdf_images/"
    print("directory with IMAGES", directory_with_new_images)
    new_images = list_files(directory_with_new_images, extension=".png")
    new_images_iter = iter(new_images)


    for image_name in new_images:
        print(image_name)



    for rst_filename in list_files(directory_to_update, extension=".rst"):
        filepath = os.path.join(directory_to_update, rst_filename)
        print("new_images_iter", new_images_iter)
        update_rst_file(filepath, new_images_iter)


if __name__ == "__main__":
    # Set the current directory to the directory of the Python script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()
