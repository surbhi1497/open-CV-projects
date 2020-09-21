# how to draw shapes and texts on images
import cv2
import numpy as np
# shapes on images
# matrix of zeroes
img = np.zeros((512,512,3),np.uint8)
# print(img.shape)
# img.shape[0] is height and img.shape[1] is width
# to draw a line
cv2.line(img, (0, 0), (img.shape[0], img.shape[1]),
         (0, 255, 0), 3)
# to draw a rectangle
# to fill the rectangle cv2.FILLED
cv2.rectangle(img, (0, 0),(250, 350), (0, 0 , 255), cv2.FILLED)

# circle on image
cv2.circle(img, (400, 50), 30, (255,255,0),5)

# text on image
cv2.putText(img, "OPENCV" , (300,300), cv2.FONT_HERSHEY_COMPLEX, 2, (0,150,0), 1)

cv2.imshow("Image ", img)
cv2.waitKey(0)
