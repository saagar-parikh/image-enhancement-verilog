'''
'''
import numpy as np
from matplotlib import pyplot as plt
import cv2

path = "1.png"                                      # Path of original image
img_orig = cv2.imread(path)                         # Creates an image object

img = cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY )   # Converting RGB to gray
cv2.imshow("Original", img)                         # Display original image

# Plot Histogram of original image--------------------------------------------

plt.hist(img.flatten(),256,[0,256], color = 'r')    # Converts image into 1D array and plot histogram
plt.xlim([0,256])                                   # Limits the x axis values to 256
plt.title("Histogram of original image")            # Title of histogram
#plt.savefig("./1-orig-hist.png", dpi=200)               # Save histogram
plt.show()                                          # Show histogram


# Double Plateus Histogram equalization---------------------------------------
origfreq = np.zeros((256,),dtype=np.float16)        # vector consisting of initial frequencies of gray scale values
newfreq = np.zeros((256,),dtype=np.float16)         # empty vector to store final frequencies of gray scale values
newgrayval = np.zeros((256,),dtype=np.float16)      # vector consisting of final gray scale values
height, width = img.shape                           # Find height and width of image 
print(img.shape)

# for loop to count frequency of gray scale values
for i in range(width):                         
    for j in range(height):
        g = img[j,i]                                # g is grayscale value of pixel
        origfreq[g] = origfreq[g]+1                 # add 1 to count of frequency

# reciprocal of total number of pixels
tmp = 1.0/(height*width)

# Tup = Upper Threshold value
# Tdown = Lower Threshold value
# Calculate Tup
count=0
total=0
not_zero=0
for k in range(0,256):
    if origfreq[k]!=0:
        not_zero+=1
    if k<255 and k>=1 and origfreq[k+1]!=0 or origfreq[k-1]!=0:
        if (origfreq[k]>origfreq[k+1] or origfreq[k]>origfreq[k-1]):
            count+=1
            total+=origfreq[k]
           

Tup = total/count
#Tup=2500
print('Tup',Tup)

# Calculate Tdown using Tup
Tdown = (np.min((1/tmp, not_zero*Tup )))/(255)
print('Tdown',Tdown)


# Clipping
excess=0                                        # no. of excess pixels (above Tup) for a bin
deficit=0                                       # no. of deficit pixels (below Tdown) for a bin
to_add=[]
to_subtract=[]
for k in range(0,256):
    if origfreq[k]==0:
        newfreq[k]=origfreq[k]
        to_add+=[k]
    elif origfreq[k]<Tdown:
        deficit += Tdown - origfreq[k]
        newfreq[k]=Tdown
    elif origfreq[k]>Tdown and origfreq[k]<Tup:
        newfreq[k]=origfreq[k]
        to_add+=[k]
        to_subtract+=[k]
    else:# origfreq[k] > Tup
        excess += origfreq[k] - Tup
        newfreq[k] = Tup
        
# Redistribute excess pixels into other bins----------------------------------
for i in to_add:
    if newfreq[i]<Tup:
        newfreq[i]+=excess/len(to_add)
        
for i in to_subtract:
    if newfreq[i]>Tdown:
        newfreq[i]-=deficit/len(to_subtract)

# Plot the new frequencies
plt.plot(newfreq)
plt.title("Clipped frequencies graph")
#plt.savefig("./1-clipped-freq-graph.png", dpi=200)               # Save graph
plt.show()


# for loop to calculate final gray scale values-------------------------------
for i in range(256):                           
    for j in range(i+1):                            # calculates cdf value  
        newgrayval[i] += newfreq[j] * tmp;                    
    newgrayval[i] = round(newgrayval[i] * 255)      # final gray scale value = cdf*(L-1)

# b now contains the equalized histogram
newgrayval=newgrayval.astype(np.uint8)

# Re-map values from equalized histogram into the image   
for i in range(width):                         
    for j in range(height):
        g = img[j,i]
        img[j,i]= newgrayval[g]
        

# Plot Histogram of enhanced image--------------------------------------------

plt.hist(img.flatten(),256,[0,256], color = 'r')    # Converts image into 1D array and plot histogram
plt.xlim([0,256])                                   # Limits the x axis value to 256
plt.title("Histogram after DPHE")                   # Title of histogram
#plt.savefig("./1-dphe-hist.png", dpi=200)     # Save histogram
plt.show()                                          # Display histogram

'''
# Plot Histogram of equalized image-------------------------------------------
equ = cv2.equalizeHist(img)
plt.hist(equ.flatten(),256,[0,256], color = 'r')    # Converts image into 1D array and plot histogram
plt.xlim([0,256])                                   # Limits the x axis values to 256
plt.title("Histogram after HE")                     # Title of histogram
#plt.savefig("./8-hist.png", dpi=200)               # Save histogram
plt.show()   
#-----------------------------------------------------------------------------
'''

#Display all images-----------------------------------------------------------

cv2.imshow("After DPHE", img)             # To display the enhanced image (manual Histogram equalization)
#cv2.imwrite("1-dphe-img.png", img)
# cv2.imshow("After HE", equ)             # To display the enhanced image (manual Histogram equalization)

cv2.waitKey(0)
