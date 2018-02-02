import cv2 as cv
import numpy as np

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

img = cv.imread('../../../IMAGES/affine_input.png')
rows,cols,ch = img.shape

pts1 = np.float32([[42,150],[42,44],[146,44]])
pts2 = np.float32([[50,200],[10,100],[100,20]])

M = cv.getAffineTransform(pts1,pts2)

dst = cv.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()