import re

def update_image_references(file_path, image_names):
    # Read the content of the file
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return
    except IOError:
        print(f"Error opening or reading the file {file_path}.")
        return

    # Compile a regular expression pattern to match figure references
    pattern = re.compile(r'\.\. figure:: _static/pdf_images/(page_\d+_image_\d+\.png)')

    # Initialize an iterator over the list of new image names
    image_names_iter = iter(image_names)

    # Function to be used as replacement in re.sub
    def replacement(match):
        try:
            # Get the next image name from the iterator
            new_image_name = next(image_names_iter)
        except StopIteration:
            print("Ran out of new image names.")
            return match.group(0)  # Return the original match if no more images
        # Return the updated figure reference
        return f".. figure:: _static/pdf_images/{new_image_name}"

    # Replace the matched patterns with the new image names
    updated_content = pattern.sub(replacement, content)

    # Write the updated content back to the file or a new file
    try:
        with open(file_path.replace('.txt', '_updated.txt'), 'w', encoding='utf-8') as file:
            file.write(updated_content)
    except IOError:
        print(f"Error writing the updated content to {file_path}.")
        return

    print(f"Updated file has been saved as {file_path.replace('.txt', '_updated.txt')}")

# Example usage
file_path = 'index_Copy.rst'  # Path to your file
image_names= [
    "page_8_image_1.png", "page_8_image_2.png", "page_9_image_1.png", "page_10_image_1.png",
    "page_10_image_2.png", "page_11_image_1.png", "page_11_image_2.png", "page_11_image_3.png",
    "page_12_image_1.png", "page_12_image_2.png", "page_13_image_1.png", "page_14_image_1.png",
    "page_15_image_1.png", "page_15_image_2.png", "page_16_image_1.png", "page_16_image_2.png",
    "page_17_image_1.png", "page_17_image_2.png", "page_18_image_1.png", "page_18_image_2.png",
    "page_19_image_1.png", "page_19_image_2.png", "page_20_image_1.png", "page_20_image_2.png",
    "page_21_image_1.png", "page_21_image_2.png", "page_22_image_1.png", "page_22_image_2.png",
    "page_23_image_1.png", "page_23_image_2.png", "page_24_image_1.png", "page_24_image_2.png",
    "page_25_image_1.png", "page_25_image_2.png", "page_26_image_1.png", "page_26_image_2.png",
    "page_27_image_1.png", "page_27_image_2.png", "page_28_image_1.png", "page_28_image_2.png",
    "page_29_image_1.png", "page_29_image_2.png", "page_29_image_3.png", "page_30_image_1.png",
    "page_30_image_2.png", "page_31_image_1.png", "page_31_image_2.png", "page_32_image_1.png",
    "page_32_image_2.png", "page_33_image_1.png", "page_33_image_2.png", "page_33_image_3.png",
    "page_34_image_1.png", "page_34_image_2.png", "page_35_image_1.png", "page_35_image_2.png",
    "page_36_image_1.png", "page_36_image_2.png", "page_36_image_3.png", "page_37_image_1.png",
    "page_37_image_2.png", "page_38_image_1.png", "page_38_image_2.png", "page_39_image_1.png",
    "page_39_image_2.png", "page_40_image_1.png", "page_40_image_2.png", "page_41_image_1.png",
    "page_42_image_1.png", "page_42_image_2.png", "page_43_image_1.png", "page_44_image_1.png",
    "page_44_image_2.png", "page_45_image_1.png", "page_45_image_2.png", "page_46_image_1.png",
    "page_46_image_2.png", "page_47_image_1.png", "page_47_image_2.png", "page_48_image_1.png",
    "page_48_image_2.png", "page_49_image_1.png", "page_49_image_2.png", "page_49_image_3.png",
    "page_50_image_1.png", "page_50_image_2.png", "page_51_image_1.png", "page_52_image_1.png",
    "page_52_image_2.png", "page_53_image_1.png", "page_53_image_2.png", "page_54_image_1.png",
    "page_54_image_2.png", "page_55_image_1.png", "page_55_image_2.png", "page_56_image_1.png",
    "page_56_image_2.png", "page_57_image_1.png", "page_57_image_2.png", "page_58_image_1.png",
    "page_58_image_2.png", "page_59_image_1.png", "page_59_image_2.png", "page_60_image_1.png",
    "page_61_image_1.png", "page_61_image_2.png", "page_62_image_1.png", "page_62_image_2.png",
    "page_63_image_1.png", "page_64_image_1.png", "page_64_image_2.png", "page_65_image_1.png",
    "page_65_image_2.png", "page_66_image_1.png", "page_67_image_1.png", "page_67_image_2.png",
    "page_68_image_1.png", "page_68_image_2.png", "page_69_image_1.png", "page_69_image_2.png",
    "page_70_image_1.png", "page_70_image_2.png", "page_71_image_1.png", "page_71_image_2.png",
    "page_72_image_1.png", "page_72_image_2.png", "page_73_image_1.png", "page_73_image_2.png",
    "page_73_image_3.png", "page_74_image_1.png", "page_74_image_2.png", "page_75_image_1.png",
    "page_75_image_2.png", "page_76_image_1.png", "page_77_image_1.png", "page_77_image_2.png",
    "page_78_image_1.png", "page_78_image_2.png", "page_79_image_1.png", "page_79_image_2.png",
    "page_80_image_1.png", "page_81_image_1.png", "page_81_image_2.png", "page_82_image_1.png",
    "page_83_image_1.png", "page_83_image_2.png", "page_84_image_1.png", "page_84_image_2.png",
    "page_86_image_1.png", "page_86_image_2.png", "page_87_image_1.png", "page_87_image_2.png",
    "page_88_image_1.png", "page_88_image_2.png", "page_89_image_1.png", "page_90_image_1.png",
    "page_90_image_2.png", "page_91_image_1.png", "page_91_image_2.png", "page_91_image_3.png",
    "page_92_image_1.png", "page_92_image_2.png", "page_93_image_1.png"
]

print(len(image_names))
# update_image_references(file_path, image_names)
