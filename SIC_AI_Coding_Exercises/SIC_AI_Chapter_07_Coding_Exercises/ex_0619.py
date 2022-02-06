"""Coding Practice #0619."""

import cv2

# Open an image B/W.
img = cv2.imread('picture_LenaSoderberg.jpg', 0)

# 1. Thresholding.

# 1.1. Binary thresholding.
threshold_val = 80
max_val = 255  # Maximum value.
_, img_bin = cv2.threshold(img, threshold_val, max_val, cv2.THRESH_BINARY)
cv2.imshow("Lena Soderberg Binary Thresholding", img_bin)
cv2.waitKey(0)  # Wait until a key is pressed.
cv2.destroyAllWindows()  # Close the open window.

# 1.2. Adaptive thresholding.
max_val = 255  # Maximum value.
block_size = 55  # Block size considered for calculating the threshold value. Has to be an odd number.
mean_reference = 0  # Constant subtracted form the local mean (threshold).
img_adapt = cv2.adaptiveThreshold(img, max_val, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, mean_reference)
cv2.imshow("Lena Soderberg Adaptive Thresholding", img_adapt)
cv2.waitKey(0)  # Wait until a key is pressed.
cv2.destroyAllWindows()  # Close the open window.
