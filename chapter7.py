# color detection
import cv2
import numpy as np
img = cv2.imread("Resources/car.jpg")
'''imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("Original ",img)
cv2.imshow("HSV image",imgHSV)'''

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
def empty(a):
    pass
cv2.namedWindow("TrackBars")

cv2.resizeWindow("TrackBars", 320,480)
cv2.createTrackbar("Hue MIn", "TrackBars",0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars",179, 179, empty)
cv2.createTrackbar("Sat MIn", "TrackBars",0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars",255, 255, empty)
cv2.createTrackbar("Value MIn", "TrackBars",0, 255, empty)
cv2.createTrackbar("Value Max", "TrackBars",255, 255, empty)

#cv2.imshow("HSV image",imgHSV)
while True:
    img = cv2.imread("Resources/car.jpg")
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue MIn", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat MIn", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Value MIn", "TrackBars")
    v_max = cv2.getTrackbarPos("Value Max", "TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("original", img)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("Bitwise", imgResult)
    cv2.waitKey(1)