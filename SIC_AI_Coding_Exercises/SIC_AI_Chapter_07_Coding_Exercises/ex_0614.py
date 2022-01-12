# Coding Practice #0614
#----------------------------------------------------------------------------------

# Install OpenCV first.
# At the Anaconda prompt do: pip install opencv-contrib-python

import numpy as np
import cv2

# Let's check for the OpvenCV version.
print('OpenCV version : ', cv2.__version__)

# Go to the directory where the data file is located. 
# os.chdir(r'~~')                     				  # Please, replace the path with your own.   

# 1. Working with image data.
# 1.1. Open an image in B/W and show it.
img = cv2.imread('picture_Butterfly.jpg',0)         			  # Open as a black and white image. 
print("Shape of the image read in B/W : ", img.shape)                        # Height, width.

cv2.imshow("A B/W Image", img)
cv2.waitKey(0)                                                                          # Wait until a key is pressed.
cv2.destroyAllWindows()                                                             # Close the open window.

# 1.2. Open an image in color and show it.
img = cv2.imread('picture_Butterfly.jpg',1)         			   # Open as a color image.
print("Shape of the image read in color : ", img.shape)                        # Height, width, channel

cv2.imshow("A Color Image", img)
cv2.waitKey(0)                                                                          # Wait until a key is pressed.
cv2.destroyAllWindows()                                                             # Close the open window.

# 1.3. Split the color channels (BGR and not RGB).
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]
zeros = 0*b.copy()                                                                    # Same shape filled with 0s. 

blue_channel = cv2.merge([b, zeros, zeros]) 
green_channel = cv2.merge([zeros,g,zeros]) 
red_channel = cv2.merge([zeros,zeros,r]) 

cv2.imshow("The Blue Channel", blue_channel)
cv2.waitKey(0)                                                                          # Wait until a key is pressed.
cv2.destroyAllWindows()                                                             # Close the open window.

cv2.imshow("The Green Channel", green_channel)
cv2.waitKey(0)                                                                          # Wait until a key is pressed.
cv2.destroyAllWindows()                                                             # Close the open window.

cv2.imshow("The Red Channel", red_channel)
cv2.waitKey(0)                                                                          # Wait until a key is pressed.
cv2.destroyAllWindows()                                                             # Close the open window.

# 1.4. Saving the image data in external files.
cv2.imwrite("picture_Butterfly_blue.jpg", blue_channel)
cv2.imwrite("picture_Butterfly_green.jpg", green_channel)
cv2.imwrite("picture_Butterfly_red.jpg", red_channel)
