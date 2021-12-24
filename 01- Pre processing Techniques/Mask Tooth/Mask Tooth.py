import cv2
import numpy as np

img1 = cv2.imread('images/12.jpg', 0)
img2 = cv2.imread('images/13.jpg', 0)

rows , cols = img2.shape

for i in range(rows):
    for j in range(cols):
        if img2[i][j] <= 254:
            img2[i][j] = 0

for i in range(rows):
    for j in range(cols):
        if img2[i][j] == 255:
            img2[i][j] = 1

result = img1 * img2

cv2.imwrite('result.jpg' , result)
cv2.imshow('result' , result)

cv2.waitKey()
