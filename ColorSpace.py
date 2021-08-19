import numpy as np
import cv2

# LOAD AN IMAGE USING 'IMREAD'
image = cv2.imread("C:/Users/Bushra Fatima/Documents/capsule.jpeg")

#TO BGR
low_green=np.array([50,90,90])
high_green=np.array([90,130,130])
green_mask=cv2.inRange(image,low_green,high_green)
rgb_green=cv2.bitwise_and(image, image, mask=green_mask)
cv2.imshow("image", image)
cv2.imshow("BGR", rgb_green)
cv2.waitKey(0)

#TO HSV
hsv_image=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
low_green=np.array([45,40,80])
high_green=np.array([80,255,255])
green_mask=cv2.inRange(image,low_green,high_green)
hsv_green=cv2.bitwise_and(image, image, mask=green_mask)

cv2.imshow("HSV", hsv_green)
cv2.waitKey(0)


#TO YCrCb

hsv_image=cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
low_green=np.array([55,100,100])
high_green=np.array([110,150,150])
green_mask=cv2.inRange(image,low_green,high_green)
YCrCb_green=cv2.bitwise_and(image, image, mask=green_mask)
cv2.imshow("YCrCb", YCrCb_green)
cv2.waitKey(0)
