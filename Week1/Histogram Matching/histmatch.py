# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 23:34:35 2020

@author: saagar.parikh
"""
import numpy as np
from matplotlib import pyplot as plt
import cv2

path_target="target.jpeg"
target_img = cv2.imread(path_target)           # Target image
#print(target_img.shape)                       # Check the size of the image

target_img = cv2.cvtColor(target_img, cv2.COLOR_BGR2GRAY )    # Converting RGB to gray
target_img1=target_img
target_img2=target_img

path_ref="ref.jpeg"
img1 = cv2.imread(path_ref)                               
ref_img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY )    # Reference image

#Display target and reference images
cv2.imshow("Target image original", target_img) 
cv2.imshow("Reference image original", ref_img)

plt.hist(target_img.flatten(),256,[0,256], color = 'r')     # Converts image into 1D array and plot histogram
plt.xlim([0,256])                                           # Limits the x axis value to 256
plt.title("Histogram of orig target image")                 # Title of histogram
plt.savefig("./target-orig-hist.png", dpi=200)              # Save histogram
plt.show()                                                  # Display histogram


# Performing Equalisation on original image-----------------------------------

target_freq = np.zeros((256,),dtype=np.float16)             # vector consisting of initial frequencies of gray scale values
target_new_grayval = np.zeros((256,),dtype=np.float16)      # vector consisting of final gray scale values

height, width = target_img.shape                            # Find height and width of image 

max1 = 0
# for loop to count frequency of gray scale values
for i in range(width):                         
    for j in range(height):
        g = target_img[j,i]                                 # g is grayscale value of pixel
        target_freq[g] = target_freq[g]+1                   # adds 1 to count of frequency     
        if g>max1:
            max1=g
            
#print(max1)
# reciprocal of total number of pixels
tmp = 1.0/(height*width)                       

# for loop to calculate final gray scale values
for i in range(256):                           
    for j in range(i+1):                                            # calculates cdf value  
        target_new_grayval[i] += target_freq[j] * tmp;                    
    target_new_grayval[i] = round(target_new_grayval[i] * 255)      # final gray scale value = cdf(L-1)

# b now contains the equalized histogram
target_new_grayval=target_new_grayval.astype(np.uint8)

# Re-map values from equalized histogram into the image   
for i in range(width):                         
    for j in range(height):
        g = target_img[j,i]
        target_img1[j,i]= target_new_grayval[g]
        

#cv2.imshow("Target image after eq", target_img1)        

"""

plt.hist(target_img1.flatten(),256,[0,256], color = 'r')   # Converts image into 1D array and plot histogram
plt.xlim([0,256])                                   # Limits the x axis value to 256
plt.title("Histogram of target image after eq")            # Title of histogram
plt.show()                                          # Display histogram
"""


# Histogram Equalisation of Reference Image-----------------------------------------------

ref_freq = np.zeros((256,),dtype=np.float16)                # vector consisting of initial frequencies of gray scale values
ref_new_grayval = np.zeros((256,),dtype=np.float16)         # vector consisting of final gray scale values

height, width = ref_img.shape                               # Find height and width of image 

max1 = 0
# for loop to count frequency of gray scale values
for i in range(width):                         
    for j in range(height):
        g = ref_img[j,i]                                    # g is grayscale value of pixel
        ref_freq[g] = ref_freq[g]+1                         # adds 1 to count of frequency     
        if g>max1:
            max1=g
#print(max1)
# reciprocal of total number of 
tmp = 1.0/(height*width)                       

# for loop to calculate final gray scale values
for i in range(256):                           
    for j in range(i+1):                                    # calculates cdf value  
        ref_new_grayval[i] += ref_freq[j] * tmp;                    
    ref_new_grayval[i] = round(ref_new_grayval[i] * 255)    # final gray scale value = cdf(L-1)

# b now contains the equalized histogram
ref_new_grayval=ref_new_grayval.astype(np.uint8)

# Re-map values from equalized histogram into the image   
for i in range(width):                         
    for j in range(height):
        g = ref_img[j,i]
        ref_img[j,i]= ref_new_grayval[g]

#cv2.imshow("Reference image after eq", ref_img)
# Histogram matching----------------------------------------------------------

target_match_intensity = np.zeros((256,),dtype=np.float16)  # vector consisting of final gray scale values

for i in range(256):
    j=0
    #print(i,ref_new_grayval[i])
    while j<256 and ref_new_grayval[i]>target_new_grayval[j]:
        j+=1
    target_match_intensity[i]=j
    #print(i,ref_new_grayval[i])
    
for i in range(width):                         
    for j in range(height):
        g = target_img[j,i]
        target_img2[j,i]= target_match_intensity[g]

#plot histograms--------------------------------------------------------------


plt.hist(ref_img.flatten(),256,[0,256], color = 'r')        # Converts image into 1D array and plot histogram
plt.xlim([0,256])                                           # Limits the x axis value to 256
plt.title("Histogram of orig reference image")              # Title of histogram
#plt.savefig("./ref-hist.png", dpi=200)                     # Save histogram
plt.show()                                                  # Display histogram


plt.hist(target_img2.flatten(),256,[0,256], color = 'r')    # Converts image into 1D array and plot histogram
plt.xlim([0,256])                                           # Limits the x axis value to 256
plt.title("Histogram of target image after histogram matching")            # Title of histogram
#plt.savefig("./target-match-hist.png", dpi=200)            # Save histogram
plt.show()                                                  # Display histogram

# ------------------------------------------------------------------------------------

cv2.imshow("Target image after matching", target_img2)
#cv2.imwrite("target-after-hist-match.jpeg", target_img2)
cv2.waitKey(0)

# References:
#
# 1. Manual histogram equalization algorithm:-
# https://stackoverflow.com/questions/50578876/histogram-equalization-using-python-and-opencv-without-using-inbuilt-functions
#
# 2. Plot histograms:-
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_histograms/py_histogram_equalization/py_histogram_equalization.html
#
# 3. Histogram matching algorithm:-
# https://youtu.be/WXHFmJVHvag

