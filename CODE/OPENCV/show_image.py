import cv2 as cv
 
#read image
#leer imagen
img = cv.imread('sample.jpg')
 
#display for 2 secs
#desplegar por 2 segundos
cv.imshow('Image', img)
cv.waitKey(2000)