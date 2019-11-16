
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
#for i, pixel in enumerate(im.getdata()):
#    print(pixel)
class eyeData():
    def __init__(self,image):
        self.width = image.width
        self.height = image.height
    def setFrame(self,df):
        self.df = df
        
    def convert2Gray(self):
        self.df.loc[:,'red'] *= 0.2989
        self.df.loc[:,'green'] *= 0.5870
        self.df.loc[:,'blue'] *= 0.1140
        
    def setGrid(self):
        zRed = np.zeros((self.height+1,self.width+1))
        redVals = self.df['red'].tolist()
        ctr = 0 
        for x in self.df['x'].tolist():
            for y in self.df['y'].tolist():
                zRed[y,x] = redVals[ctr]
                ctr+=1
        #x = df['x'].tolist()
        #y = df['y'].tolist()
        #zRed[y,x] = df['red'].tolist()
        print(zRed)
    
def image2matrix(imagePath = "Ryan's Eye 1.jpg"):
    colourImg = Image.open(imagePath)
    colourPixels = colourImg.convert("RGB")
    colourArray = np.array(colourPixels.getdata()).reshape(colourImg.size + (3,))
    indicesArray = np.moveaxis(np.indices(colourImg.size), 0, 2)
    allArray = np.dstack((indicesArray, colourArray)).reshape((-1, 5))


    df = pd.DataFrame(allArray, columns=["y", "x", "red","green","blue"])
    eyeDat = eyeData(colourImg)
    eyeDat.setFrame(df)
    eyeDat.convert2Gray()
    
    return eyeDat

def plotPixels(eyeDat):
    plt.imshow((eyeDat.df['x'],eyeDat.df['y'],eyeDat.RGB))

    
# In[4]:
eye = image2matrix()
eye.setGrid()
#plotPixels(eye)


