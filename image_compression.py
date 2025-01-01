# import PIL

# from PIL import Image
# from tkinter.filedialog import *
# fl = askopenfilename()

# img = Image.open(fl[0])

# img.save("example.jpg", "JPEG", optimize=True, quality=10)
# Image.open("example.jpg")



from PIL import Image
from tkinter.filedialog import askopenfilename

# Open file dialog to select an image file
fl = askopenfilename(title="Select an image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])

if fl:  # Check if a file was selected
    # Open the selected image
    img = Image.open(fl)

    # Save the image with reduced quality
    img.save("example.jpg", "JPEG", optimize=True, quality=10)

    # Open and display the saved image
    compressed_img = Image.open("example.jpg")
    compressed_img.show()
else:
    print("No file selected.")
