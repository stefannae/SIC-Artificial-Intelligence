# Coding Practice #0616
#----------------------------------------------------------------------------------

import numpy as np
import cv2

# Go to the directory where the data file is located. 
# os.chdir(r'~~')                     				  # Please, replace the path with your own.   

# 1. Convolutional filtering.
# Open an image in B/W (Gray scale) and show it. 
img = cv2.imread('picture_LenaSoderberg_small.jpg',0)                              # Open as a B/W image.
cv2.imshow("In Gray Scale", img)
cv2.waitKey(0)                                                                          # Wait until a key is pressed.
cv2.destroyAllWindows()                                                             # Close the open window.

# 1.1. Applying the Gaussian blur kernel.
img_blurred = cv2.GaussianBlur(img, ksize=(5,5), sigmaX=10, sigmaY=10)
cv2.imshow("Blurred", img_blurred)
cv2.waitKey(0)                                                                          # Wait until a key is pressed.
cv2.destroyAllWindows()                                                             # Close the open window.

# 1.2. Applying the Sharpening kernel.
kernel_sharp = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
img_sharp = cv2.filter2D(img, ddepth = -1, kernel=kernel_sharp)          # ddepth = -1 => the destination has the same depth as the source image.
cv2.imshow("Sharpened", img_sharp)
cv2.waitKey(0)                                                                          # Wait until a key is pressed.
cv2.destroyAllWindows()                                                             # Close the open window.

# 1.3. Applying the Outline kernel #1.
kernel_outline1 = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
img_outlined1 = cv2.filter2D(img, ddepth = -1, kernel=kernel_outline1)  # ddepth = -1 => the destination has the same depth as the source image.
cv2.imshow("Outlined #1", img_outlined1)
cv2.waitKey(0)                                                                           # Wait until a key is pressed.
cv2.destroyAllWindows()                                                              # Close the open window.

# 1.4. Applying the Outline kernel #2.
kernel_outline2 = np.array([[0,1,0],[1,-4,1],[0,1,0]])
img_outlined2 = cv2.filter2D(img, ddepth = -1, kernel=kernel_outline2)    # ddepth = -1 => the destination has the same depth as the source image.
cv2.imshow("Outlined #2", img_outlined2)
cv2.waitKey(0)                                                                          # Wait until a key is pressed.
cv2.destroyAllWindows()                                                             # Close the open window.

