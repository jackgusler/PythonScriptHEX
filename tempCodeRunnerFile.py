from PIL import Image
import webcolors
import os

# Load the image
image_path = 'Images/nature_palette.webp'
image = Image.open(image_path)

# Define the number of rows and columns
rows = 3
columns = 10

# Define the starting point offsets (use the values obtained from the click script)
start_x = 105  # Replace with the actual x coordinate
start_y = 490  # Replace with the actual y coordinate

# Calculate the width and height of each color block
block_width = 105  # Distance between the start of each block horizontally
block_height = 150  # Distance between the start of each block vertically

# Extract and print the hex values
hex_colors = []
for row in range(rows):
    for col in range(columns):
        # Calculate the center of the block
        x = start_x + col * block_width
        y = start_y + row * block_height
        # Print the coordinates being used
        print(f'Coordinates: x={x}, y={y}')
        # Get the color at the center of the block
        color = image.getpixel((x, y))
        # Print the RGB color being extracted
        print(f'Extracted RGB: {color[:3]}')
        # Convert RGB to HEX
        hex_color = webcolors.rgb_to_hex(color[:3])
        hex_colors.append(hex_color)
        print(f'RGB: {color[:3]}, HEX: {hex_color}')

# Optionally save the hex colors to a file
with open('extracted_hex_colors.txt', 'w') as file:
    for hex_color in hex_colors:
        file.write(f'{hex_color}\n')