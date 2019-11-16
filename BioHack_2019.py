
# coding: utf-8

# In[2]:

#imports 
import numpy as np
import pandas as pd
from matplotlib.figure import Figure 
import matplotlib.pyplot as plt
from PIL import Image

# In[3]:
#cell block for opening image file to pixel coordinates
im = Image.open("Ryan's Eye 1.jpg")

pixels = list(im.getdata())
width, height = im.size

for i, pixel in enumerate(im.getdata()):
    print(pixel)

# In[4]:



