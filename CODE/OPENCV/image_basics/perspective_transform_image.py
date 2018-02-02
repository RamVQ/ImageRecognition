img = cv2.imread('..\..\..\IMAGES\sudokusmall.png')
rows,cols,ch = img.shape

pts1 = np.float32([[29,200],[208,202],[42,42],[197,37]])
pts2 = np.float32([[0,300],[300,300],[0,0],[300,0]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()