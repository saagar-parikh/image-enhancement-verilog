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
        if int(img[j][i]) < 2:
            b= str(bin(img[j][i]))
            img1 =   img1 + "0000000" + b[2:] +"\n"
        elif int(img[j][i]) < 4:
            b= str(bin(img[j][i]))
            img1 =  img1 + "000000" + b[2:] +"\n" 
        elif int(img[j][i]) < 8:
            b= str(bin(img[j][i]))
            img1 = img1 + "00000" + b[2:]+"\n" 
        elif int(img[j][i]) < 16:
            b= str(bin(img[j][i]))
            img1 = img1 + "0000" + b[2:]+"\n"
        elif int(img[j][i]) < 32:
            b= str(bin(img[j][i]))
            img1 = img1 + "000" + b[2:] + "\n" 
        elif int(img[j][i]) < 64:
            b= str(bin(img[j][i]))
            img1 = img1 + "00" + b[2:] + "\n" 
        elif int(img[j][i]) < 128:
            b= str(bin(img[j][i]))
            img1 =  img1 + "0" + b[2:] + "\n" 
        else:
            b= str(bin(img[j][i]))
            img1 =  img1 +  b[2:] + "\n"

file = open("4119_binary.txt", "w")
# file.write(img1)
file.close()

            
#print(img1)
#img_String=''
#for i in range(width):                         
 #   for j in range(height):
  #      img_String= img_String + str(img1[j][i])
        
#img_String.replace("0x","")
#print(img_String)
        
        