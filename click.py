import matplotlib.pyplot as plt
from PIL import Image

# Load the image
image_path = 'Images/nature_palette.webp'
image = Image.open(image_path)

# Display the image
fig, ax = plt.subplots()
ax.imshow(image)

# Function to print the coordinates of the clicked point
def onclick(event):
    x, y = event.xdata, event.ydata
    print(f'Clicked coordinates: x={x}, y={y}')
    plt.close()

# Connect the click event to the function
cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()

# Coordinates: x=155, y=575
# Extracted RGB: (102, 160, 72)
# RGB: (102, 160, 72), HEX: #66a048
# Coordinates: x=255, y=575
# Extracted RGB: (159, 191, 203)
# RGB: (159, 191, 203), HEX: #9fbfcb
# Coordinates: x=355, y=575
# Extracted RGB: (186, 203, 213)
# RGB: (186, 203, 213), HEX: #bacbd5
# Coordinates: x=455, y=575
# Extracted RGB: (51, 91, 114)
# RGB: (51, 91, 114), HEX: #335b72
# Coordinates: x=555, y=575
# Extracted RGB: (188, 218, 233)
# RGB: (188, 218, 233), HEX: #bcdae9
# Coordinates: x=655, y=575
# Extracted RGB: (160, 194, 205)
# RGB: (160, 194, 205), HEX: #a0c2cd
# Coordinates: x=755, y=575
# Extracted RGB: (79, 96, 106)
# RGB: (79, 96, 106), HEX: #4f606a
# Coordinates: x=855, y=575
# Extracted RGB: (112, 139, 146)
# RGB: (112, 139, 146), HEX: #708b92
# Coordinates: x=955, y=575
# Extracted RGB: (169, 173, 176)
# RGB: (169, 173, 176), HEX: #a9adb0
# Coordinates: x=1055, y=575
# Extracted RGB: (101, 125, 131)
# RGB: (101, 125, 131), HEX: #657d83
# Coordinates: x=155, y=725
# Extracted RGB: (211, 185, 162)
# RGB: (211, 185, 162), HEX: #d3b9a2
# Coordinates: x=255, y=725
# Extracted RGB: (185, 146, 123)
# RGB: (185, 146, 123), HEX: #b9927b
# Coordinates: x=355, y=725
# Extracted RGB: (254, 254, 254)
# RGB: (254, 254, 254), HEX: #fefefe
# Coordinates: x=455, y=725
# Extracted RGB: (127, 104, 78)
# RGB: (127, 104, 78), HEX: #7f684e
# Coordinates: x=555, y=725
# Extracted RGB: (212, 212, 212)
# RGB: (212, 212, 212), HEX: #d4d4d4
# Coordinates: x=655, y=725
# Extracted RGB: (74, 78, 68)
# RGB: (74, 78, 68), HEX: #4a4e44
# Coordinates: x=755, y=725
# Extracted RGB: (114, 103, 87)
# RGB: (114, 103, 87), HEX: #726757
# Coordinates: x=855, y=725
# Extracted RGB: (207, 191, 178)
# RGB: (207, 191, 178), HEX: #cfbfb2
# Coordinates: x=955, y=725
# Extracted RGB: (186, 139, 121)
# RGB: (186, 139, 121), HEX: #ba8b79
# Coordinates: x=1055, y=725
# Extracted RGB: (125, 118, 105)
# RGB: (125, 118, 105), HEX: #7d7669
# Coordinates: x=155, y=875
# Extracted RGB: (255, 255, 255)
# RGB: (255, 255, 255), HEX: #ffffff
# Coordinates: x=255, y=875
# Extracted RGB: (255, 255, 255)
# RGB: (255, 255, 255), HEX: #ffffff
# Coordinates: x=355, y=875
# Extracted RGB: (255, 255, 255)
# RGB: (255, 255, 255), HEX: #ffffff
# Coordinates: x=455, y=875
# Extracted RGB: (255, 255, 255)
# RGB: (255, 255, 255), HEX: #ffffff
# Coordinates: x=555, y=875
# Extracted RGB: (255, 255, 255)
# RGB: (255, 255, 255), HEX: #ffffff
# Coordinates: x=655, y=875
# Extracted RGB: (255, 255, 255)
# RGB: (255, 255, 255), HEX: #ffffff
# Coordinates: x=755, y=875
# Extracted RGB: (255, 255, 255)
# RGB: (255, 255, 255), HEX: #ffffff
# Coordinates: x=855, y=875
# Extracted RGB: (255, 255, 255)
# RGB: (255, 255, 255), HEX: #ffffff
# Coordinates: x=955, y=875
# Extracted RGB: (255, 255, 255)
# RGB: (255, 255, 255), HEX: #ffffff
# Coordinates: x=1055, y=875
# Extracted RGB: (255, 255, 255)
# RGB: (255, 255, 255), HEX: #ffffff