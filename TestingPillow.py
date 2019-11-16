# coding: utf-8

# In[2]:

import numpy as np
import pandas as pd
from matplotlib.figure import Figure 
import matplotlib.pyplot as plt
from PIL import Image

path = "Ryan's Eye 1.jpg"
im = Image.open(path)
pixels = list(im.getdata())
print("**********************************")
width, height = im.size

# Open an Image
def open_image(path):
    newImage = Image.open(path)
    return newImage

# Save Image
def save_image(image):
    image.save(path, 'jpg')

# Create a new image with the given size
def create_image(i, j):
    image = Image.new("RGB", (i, j), "white")
    return image

# Get the pixel from the given image
def get_pixel(image, i, j):
    # Inside image bounds?
    width, height = image.size
    if i > width or j > height:
      return None

    # Get Pixel
    pixel = image.getpixel((i, j))
    return pixel

