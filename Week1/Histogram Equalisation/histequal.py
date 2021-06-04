# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 00:44:48 2020

@author: saagar.parikh
"""
import numpy as np
from matplotlib import pyplot as plt
import cv2

path = "8.png"                                      # Path of original image
img_orig = cv2.imread(path)                         # Creates an image object

img = cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY )   # Converting RGB to gray


#Histogram Equalization using inbuilt function--------------------------------
equ = cv2.equalizeHist(img)


#performing histogram equalization manually-----------------------------------

origfreq = np.zeros((256,),dtype=np.float16)        # vector consisting of initial frequencies of gray scale values
newgrayval = np.zeros((256,),dtype=np.float16)      # vector consisting of final gray scale values

height, width = img.shape                           # Find height and width of image 


# for loop to count frequency of gray scale values
for i in range(width):                         
    for j in range(height):
        g = img[j,i]                                # g is grayscale value of pixel
        origfreq[g] = origfreq[g]+1                 # add 1 to count of frequency

# reciprocal of total number of pixels
tmp = 1.0/(height*width)                       

# for loop to calculate final gray scale values
for i in range(256):                           
    for j in range(i+1):                            # calculates cdf value  
        newgrayval[i] += origfreq[j] * tmp;                    
    newgrayval[i] = round(newgrayval[i] * 255)      # final gray scale value = cdf*(L-1)

# b now contains the equalized histogram
newgrayval=newgrayval.astype(np.uint8)

# Re-map values from equalized histogram into the image   
for i in range(width):                         
    for j in range(height):
        g = img[j,i]
        img[j,i]= newgrayval[g]
        
#plot histograms--------------------------------------------------------------

hist,bins = np.histogram(img.flatten(),256,[0,256]) # Create histogram of original image

cdf = hist.cumsum()                                 # Computes cumulative sum of array elements
cdf_normalized = cdf * hist.max()/ cdf.max()        # Normalize cdf value

plt.hist(img.flatten(),256,[0,256], color = 'r')    # Converts image into 1D array and plot histogram
plt.xlim([0,256])                                   # Limits the x axis values to 256
plt.title("Histogram of original image")            # Title of histogram
plt.savefig("./8-hist.png", dpi=200)                # Save histogram
plt.show()                                          # Display histogram

#perform histogram equalization
cdf_temp = np.ma.masked_equal(cdf,0)                # Checks validity of cdf values and store in cdf_m ( temporary cdf for new image )
cdf_temp = (cdf_temp - cdf_temp.min())*255/(cdf_temp.max()-cdf_temp.min()) # Formula for histogram equalisation
cdf = np.ma.filled(cdf_temp,0).astype('uint8')      # Store value from cdf_m back into cdf

img2 = cdf[img]                                     # Final image
cdf_normalized = cdf * hist.max()/ cdf.max()        # Normalize cdf values

plt.hist(img2.flatten(),256,[0,256], color = 'r')   # Converts image into 1D array and plot histogram
plt.xlim([0,256])                                   # Limits the x axis value to 256
plt.title("Histogram of equalized image")           # Title of histogram
plt.savefig("./8-equalized-hist.png", dpi=200)      # Save histogram
plt.show()                                          # Display histogram


#Display all images-----------------------------------------------------------

cv2.imshow("Original Image", img_orig)                           # To display the image
cv2.imshow("After manual Histogram Equalization", img)           # To display the enhanced image (manual Histogram equalization)
cv2.imshow("After Histogram Equalization using inbuilt function", equ)   # To display the enhanced image (Histogram equalization using inbuilt function )
cv2.waitKey(0)

cv2.imwrite("8-after-manual-histequal.png", img)
cv2.imwrite("8-after-func-histequal.png", equ)

# References:
# 
# 1. Manual histogram equalization algorithm:-
# https://stackoverflow.com/questions/50578876/histogram-equalization-using-python-and-opencv-without-using-inbuilt-functions
#
# 2. Plot histograms:-
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_histograms/py_histogram_equalization/py_histogram_equalization.html