import cv2 as cv
 
img = cv.imread('sample.jpg') #read image, leer imagen
cv.imwrite('sample_copy.jpg',img) #write image, escribir imagen