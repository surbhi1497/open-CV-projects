import cv2
print('package imported')
# load image
'''img = cv2.imread("Resources/shinchan.jpg")
cv2.imshow("output",img)
cv2.waitKey(1000)'''
# load video capture
# cap = cv2.VideoCapture("Resources/snap_vid.mp4")
# load webcam if we use web cam use id as 0
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 130)
# since video is a sequence of frames
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




