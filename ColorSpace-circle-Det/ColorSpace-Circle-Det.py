import numpy as np
import cv2 as cv


# LOAD AN IMAGE USING 'IMREAD'
image = cv.imread("C:/Users/Bushra Fatima/Documents/capsule.jpeg")
#TO BGR
low_green=np.array([95,90,60])
high_green=np.array([120,115,85])
# low_green=np.array([100,95,65])
# high_green=np.array([115,110,80])
green_mask=cv.inRange(image,low_green,high_green)
#rgb_green=cv2.bitwise_and(image, image, mask=green_mask)
# gray = cv.cvtColor(green_mask, cv.COLOR_BGR2GRAY)

cv.imshow("image", image)
cv.imshow("BGR", green_mask)
cv.waitKey(0)








