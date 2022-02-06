"""Coding Practice #0618."""

import cv2

# Open an image in color.
img = cv2.imread('picture_LenaSoderberg.jpg')
cv2.imshow("Lena Soderberg", img)
cv2.waitKey(0)  # Wait until a key is pressed.
cv2.destroyAllWindows()  # Close the open window.

# 1. Transforming image data.

# 1.1. Resizing image.
img_half = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)  # (0,0) means relative size.
cv2.imshow("Smaller Image", img_half)
cv2.waitKey(0)  # Wait until a key is pressed.
cv2.destroyAllWindows()  # Close the open window.

img_stretch1 = cv2.resize(img, (0, 0), fx=1.2, fy=0.5)
cv2.imshow("Streatched Image", img_stretch1)
cv2.waitKey(0)  # Wait until a key is pressed.
cv2.destroyAllWindows()  # Close the open window.

img_stretch2 = cv2.resize(img, (0, 0), fx=0.5, fy=1.2)
cv2.imshow("Streatched Image", img_stretch2)
cv2.waitKey(0)  # Wait until a key is pressed.
cv2.destroyAllWindows()  # Close the open window.

# 1.2. Image rotation by affine transformation.
height = img.shape[0]
width = img.shape[1]

rmat = cv2.getRotationMatrix2D(center=(0, 0), angle=-15, scale=1)
img_rotated1 = cv2.warpAffine(img, rmat, (width, height))
cv2.imshow("Rotated Image (centered at the top left corner).", img_rotated1)
cv2.waitKey(0)  # Wait until a key is pressed.
cv2.destroyAllWindows()  # Close the open window.

rmat = cv2.getRotationMatrix2D(center=(width / 2, height / 2), angle=45, scale=1)
img_rotated2 = cv2.warpAffine(img, rmat, (width, height))
cv2.imshow("Rotated Image", img_rotated2)
cv2.waitKey(0)  # Wait until a key is pressed.
cv2.destroyAllWindows()  # Close the open window.
