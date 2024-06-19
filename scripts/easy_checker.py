import re
def extract_blocks(source_file_path, target_file_path):
    # Flag to indicate if the current line is within the block to extract
    in_block = False
    start_indicator = ".. figure:: _static/pdf_images/"
    end_indicator = "Figure "

    with open(source_file_path, 'r',encoding= "utf-8") as source_file, open(target_file_path, 'w', encoding= "utf-8") as target_file:
        for line in source_file:
            # Check if the line is the start of a block
            if start_indicator in line:
                in_block = True

            # Write the line to the target file if we are within a block
            if in_block:
                target_file.write(line)

            # Check if the line is the end of a block, and reset the flag
            if in_block and end_indicator in line:
                in_block = False
                # Optionally, write a separator between blocks
                target_file.write("\n\n")


# Function to read the document and extract image references
def extract_image_references_from_document(file_path):
    pattern = re.compile(r'\.\. figure:: _static/pdf_images/(page_\d+_image_\d+\.png)')
    with open(file_path, 'r') as file:
        content = file.read()
    return pattern.findall(content)


# Function to compare the extracted references with a predefined list
def compare_references(extracted_refs, predefined_list):
    matches = []
    mismatches = []

    for ref in extracted_refs:
        if ref in predefined_list:
            matches.append(ref)
        else:
            mismatches.append(ref)

    return matches, mismatches

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

# Example usage
source_file_path = 'blocks.rst'
target_file_path = 'compare_blocks.rst'
extract_blocks(source_file_path, target_file_path)


# Extract references from your document
# file_path = 'path_to_your_document.txt'  # Update this with the actual file path
extracted_image_refs = extract_image_references_from_document(source_file_path)

# Compare and report
matches, mismatches = compare_references(extracted_image_refs, image_names)

print("Matches:", len(matches))
print("Mismatches:", len(mismatches))