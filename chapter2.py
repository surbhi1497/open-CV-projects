import cv2
import numpy as np
# import image
img = cv2.imread("resources/shinchan.jpg")
kernel = np.ones((5,5), np.uint8)

# converting into gray scale
'''imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", imgGray)
cv2.waitKey((0))
'''
# blur the image
# kernel size has to be odd no
'''imgBlur = cv2.GaussianBlur(img, (7,7), 0)
cv2.imshow("Blur Image", imgBlur)
cv2.waitKey(0)
'''

# edge detector her canny edge detector
# if we increase the dimension edges will be low
'''imgCanny = cv2.Canny(img, 100, 100)
cv2.imshow("Canny Image", imgCanny)
cv2.waitKey(0)
'''

# to increase the thickness of the edge
# kernel is just a matrix with dimension and value
'''imgCanny = cv2.Canny(img, 100, 100)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=3)
# if increase iteration count, thickness will increase
cv2.imshow("Image Dialation", imgDialation)
cv2.waitKey(0)
'''

# opposite of dialation i.e erosion
imgCanny = cv2.Canny(img, 100, 100)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations= 1)
cv2.imshow("Image eroded", imgEroded)
cv2.waitKey(0)