# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 14:56:30 2020

@author: sanja
"""
import numpy as np
from matplotlib import pyplot as plt
import cv2

import binascii
img = cv2.imread('4119.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )   # Converting RGB to gray
#height, width = fi                           # Find height and width of image 
#print(filename.shape)
#with open(filename, 'rb') as f:
#    content = f.read()
#print(binascii.hexlify(content))
#print(len(content))
#print(img)
height, width = img.shape                           # Find height and width of image 

#img= str(img)
img1 = ""
#print(img1)


for i in range(width):
    for j in range(height):
        if int(img[j][i]) < 10:
            img1 = img1 + "00" + str(int(img[j][i]))
        elif int(img[j][i]) < 100:
            img1 = img1 + "0" + str(img[j][i])
        else:
            img1 = img1 + str(img[j][i])
            
#print(img1)
#img_String=''
#for i in range(width):                         
 #   for j in range(height):
  #      img_String= img_String + str(img1[j][i])
        
#img_String.replace("0x","")
#print(img_String)
        
        