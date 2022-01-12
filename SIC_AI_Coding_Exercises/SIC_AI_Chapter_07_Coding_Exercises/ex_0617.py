# Coding Practice #0617
#----------------------------------------------------------------------------------

import numpy as np
import cv2

# Go to the directory where the data file is located. 
# os.chdir(r'~~')                     				  # Please, replace the path with your own.   

# 1. Morphological filtering.
# Open an image in B/W. 
img = cv2.imread('picture_Texture.jpg',0)         
cv2.imshow("Texture", img)
cv2.waitKey(0)                                                                          # Wait until a key is pressed.
cv2.destroyAllWindows()  					  # Close the open window.   

# 1.1. Erosion and dilation:
# Erosion: Turns white pixels into black ones.
# Dilation: Turns black pixels into white ones.
kernel = np.ones((5,5),'uint8')
img_eroded = cv2.erode(img, kernel, iterations=5)                           # 'iterations' is adjustable.
img_dilated = cv2.dilate(img,kernel,iterations=5)                              # 'iterations' is adjustable.

cv2.imshow("Eroded", img_eroded)
cv2.waitKey(0)                                                                          # Wait until a key is pressed.
cv2.destroyAllWindows()  					   # Close the open window.   

cv2.imshow("Dilated", img_dilated)
cv2.waitKey(0)                                                                          # Wait until a key is pressed.
cv2.destroyAllWindows()  					  # Close the open window.   

