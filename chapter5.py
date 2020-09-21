# warp perspective
import cv2
import numpy as np

img = cv2.imread("Resources/cards.png")
width, height = 250,350
pts1 = np.float32([[80,8],[150,28],[124,124],[55,102]])

pts2 = np.float32([[0,0], [0,height],[width,height],[width,0]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", imgOutput)
cv2.waitKey(0)