# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 21:22:11 2020

@author: sanja
"""

import numpy as np
from matplotlib import pyplot as plt
import cv2
from PIL import Image as im

f = open("4119_binary.txt", "r")
Lines = f.readlines()


one_dim = []

for line in Lines:
    one_dim = one_dim + [int(line,2)]
    #print(one_dim)
width = 324
height = 256

k = 0

img = np.zeros((256, 324), dtype=np.uint8)

for i in range (width):
    for j in range (height):
        img[j][i] =  one_dim[k]
        k = k+1
print(img)
data = im.fromarray(img) 
      
    # saving the final output  
    # as a PNG file 
# data.save('gfg_dummy_pic.png') 

        