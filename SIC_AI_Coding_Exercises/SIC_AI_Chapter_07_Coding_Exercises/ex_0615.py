# Coding Practice #0615
#----------------------------------------------------------------------------------
import numpy as np
import cv2

# Go to the directory where the data file is located. 
# os.chdir(r'~~')                     				  # Please, replace the path with your own.   

# 1. Working with image data: 

# 1.1. Open an image in color (BGR) and show it. 
img_bgr = cv2.imread('picture_Butterfly.jpg',1)                                 # Open as a color image.
print("Shape of the image read in color : ", img_bgr.shape)                # Height, width, channel.

cv2.imshow("A Color Image", img_bgr)
cv2.waitKey(0)                                                                          # Wait until a key is pressed.
cv2.destroyAllWindows()                                                             # Close the open window.

# 1.2. Convert to B/W (gray scale) and show it.
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY) 

cv2.imshow("In Gray Scale", img_gray)
cv2.waitKey(0)                                                                          # Wait until a key is pressed.
cv2.destroyAllWindows()                                                             # Close the open window.

# 1.3. Convert to HSV and split the channels: Hue, Saturation, Value. 
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV) 
h = img_hsv[:,:,0]
s = img_hsv[:,:,1]
v = img_hsv[:,:,2]

hue = cv2.merge([h,h,h])
sat = cv2.merge([s,s,s])
val = cv2.merge([v,v,v])

cv2.imshow("The Hue Channel", hue)
cv2.waitKey(0)                                                                          # Wait until a key is pressed.
cv2.destroyAllWindows()                                                             # Close the open window.

cv2.imshow("The Saturation Channel", sat)
cv2.waitKey(0)                                                                          # Wait until a key is pressed.
cv2.destroyAllWindows()                                                             # Close the open window.

cv2.imshow("The Value Channel", val)
cv2.waitKey(0)                                                                          # Wait until a key is pressed.
cv2.destroyAllWindows()                                                             # Close the open window.


