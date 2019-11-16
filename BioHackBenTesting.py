
# coding: utf-8

# In[2]:

#imports 
import numpy as np
import pandas as pd
from matplotlib.figure import Figure 
import matplotlib.pyplot as plt
from PIL import Image
from astropy.visualization import make_lupton_rgb

# In[3]:
#cell block for opening image file to pixel coordinates
"""
im = Image.open("Ryan's Eye 1.jpg")

pixels = list(im.getdata())
width, height = im.size
"""

def getFrame(sec,vidcap, cv2,count):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("C:/Users/owner/Desktop/VidConvertTests/image"+str(count)+".jpg",image) #save frame as JPG file
    return hasFrames

# In[4]:
#eye = image2matrix()
#eye.setGrid()
import cv2
inputVid = "TestVid.MOV"
vidcap = cv2.VideoCapture(inputVid)

# In[5]:
sec = 0
frameRate = 30 #it will capture image in each 0.5 second
count = 1
success = getFrame(sec,vidcap,cv2,count)
while success:
    count = count + 1
    sec = sec + 1/frameRate
    sec = round(sec, 2)
    success = getFrame(sec,vidcap,cv2,count)

print("***********")
#plotPixels(eye)


