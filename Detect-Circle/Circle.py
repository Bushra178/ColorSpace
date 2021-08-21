import numpy as np
import cv2 as cv


# LOAD AN IMAGE USING 'IMREAD'
image = cv.imread("C:/Users/Bushra Fatima/Documents/capsule.jpeg")
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
output = image.copy()
gray=cv.medianBlur(gray, 5)
circle=cv.HoughCircles(gray,cv.HOUGH_GRADIENT,36,66,
                      param1=5, param2=1, minRadius=10, maxRadius=50)
detected_circles=np.uint16(np.around(circle))
for (x, y ,r) in detected_circles[0, :]:
 cv.circle(output, (x, y), r, (0, 255, 0), 2)
 cv.circle(output, (x, y), 2, (0, 255, 255), 2)
cv.imshow('output', output)
cv.waitKey(0)



