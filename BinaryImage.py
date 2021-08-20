import numpy as np
import cv2

# LOAD AN IMAGE USING 'IMREAD'
image = cv2.imread("C:/Users/Bushra Fatima/Documents/capsule.jpeg")

# TO BGR
low_green = np.array([50, 90, 90])
high_green = np.array([90, 130, 130])
green_mask = cv2.inRange(image, low_green, high_green)
# rgb_green = cv2.bitwise_and(image, image, mask=green_mask)
# grayImage = cv2.cvtColor(rgb_green, cv2.COLOR_BGR2GRAY)
# (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("image",image)
cv2.imshow("BGR",green_mask)
cv2.waitKey(0)
