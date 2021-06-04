# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 00:17:33 2020

@author: sanja
"""

import numpy as np
from matplotlib import pyplot as plt
import cv2
#import math

path = "128.png"                                           # Path of original image
img_orig = cv2.imread(path)                              # Creates an image object

img_orig = cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY )   # Converting RGB to gray

plt.hist(img_orig.flatten(),256,[0,256], color = 'r')    # Converts image into 1D array and plot histogram
plt.xlim([0,256])                                        # Limits the x axis values to 256
plt.title("Histogram of Original image")                 # Title of histogram
plt.show()                                               # Display histogram


kernel = np.ones((20,20),np.uint8)                     # Decides the Strucutring elements

# Applying the Top-Hat operation----------------------------------------------

tophat_img = cv2.morphologyEx(img_orig, cv2.MORPH_TOPHAT, kernel) 


# Displaying the images--------------------------------------------------------
cv2.imshow("original image", img_orig) 
cv2.imshow("Top Hat Transformed image", tophat_img) 
#cv2.imwrite("128-tophat-img.png", tophat_img)
cv2.waitKey(0)