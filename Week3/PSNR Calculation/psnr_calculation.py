# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 14:19:33 2020

@author: sanja
"""

import numpy as np
from matplotlib import pyplot as plt
import cv2
import math




img_enhance = cv2.imread("88_enhanced.png")                         # Creates an image object

img_enhance = cv2.cvtColor(img_enhance, cv2.COLOR_BGR2GRAY )   # Converting RGB to gray

def psnr_calculation(img, img_enhance):
    height, width = img.shape                           # Find height and width of image 
    
    square_error = 0.0
    
    for i in range(width):                         
        for j in range(height):
            square_error = square_error + (int(img[j][i]) - int(img_enhance[j][i]))**2
    
    mean_square_error = square_error/(height*width)
    
    psnr = 10*math.log((255**2/mean_square_error), 10)  
    
    print(psnr)

img_he = cv2.imread("88_he.png")                         # Creates an image object
img_he = cv2.cvtColor(img_he, cv2.COLOR_BGR2GRAY )   # Converting RGB to gray
print("PSNR Value for Histogram Equalisation ", end =" ")
psnr_calculation(img_he, img_enhance)

img_hm = cv2.imread("target-after-hist-match.jpeg")                         # Creates an image object
img_hm = cv2.cvtColor(img_hm, cv2.COLOR_BGR2GRAY )   # Converting RGB to gray
img_hm_enhance = cv2.imread("ref.jpeg")                         # Creates an image object
img_hm_enhance = cv2.cvtColor(img_hm_enhance, cv2.COLOR_BGR2GRAY )   # Converting RGB to gray
print("PSNR Value for Histogram Matching ", end =" ")
psnr_calculation(img_hm, img_hm_enhance)

img_dphe = cv2.imread("88_dphe.png")                         # Creates an image object
img_dphe = cv2.cvtColor(img_dphe, cv2.COLOR_BGR2GRAY )   # Converting RGB to gray
print("PSNR Value for Double Plateaus Histogram Equalisation ", end =" ")
psnr_calculation(img_dphe, img_enhance)

img_th = cv2.imread("88_tophat.png")                         # Creates an image object
img_th = cv2.cvtColor(img_th, cv2.COLOR_BGR2GRAY )   # Converting RGB to gray
print("PSNR Value for Top Hat Transform ", end =" ")
psnr_calculation(img_th, img_enhance)

