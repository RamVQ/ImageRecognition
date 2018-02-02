import cv2

img = cv2.imread('sample.jpg')
res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
cv2.imshow('Image', res)
cv2.waitKey(2000)
