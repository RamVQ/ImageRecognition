import cv2 as cv
import numpy as np

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

img = cv.imread('../../../IMAGES/perspective_input.png')
rows,cols,ch = img.shape

pts1 = np.float32([[29,200],[208,202],[42,42],[197,37]])
pts2 = np.float32([[0,300],[300,300],[0,0],[300,0]])

M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()