import cv2
import numpy as np

img = cv2.imread("input/1.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

result = np.zeros(img.shape)

mask = np.ones((5,5)) / 25

rows, cols = img.shape

for i in range(2, rows - 2):
    for j in range(2, cols - 2):
        small_img = img[i-2 : i+3 , j-2 : j+3]
        result[i][j]= np.sum(small_img * mask)

cv2.imwrite('output/result-mean.png',result)


