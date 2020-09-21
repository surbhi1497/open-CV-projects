import cv2


# open cv convolution
# positive x axis is towards normal x axis itself but y axis is towards normal neg y axis
# resize a image
img = cv2.imread("Resources/shinchan.jpg")
'''
# print the size
print(img.shape)
# resize it
imgReSize = cv2.resize(img, (480, 360))
cv2.imshow("ReSized Image",imgReSize)
print(imgReSize.shape)
# cv2.imshow("output",img)
cv2.waitKey(1000)
'''
# image crop function, height come first then width
imgCropped = img[0:200, 200:500]
cv2.imshow("Cropped Image ",imgCropped)
cv2.waitKey(0)

