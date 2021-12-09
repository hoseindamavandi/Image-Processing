import cv2
import numpy as np
img = []
result = []

for i in range(15):
    images = cv2.imread(f'h{i}.jpg')
    images = cv2.cvtColor(images,cv2.COLOR_RGB2GRAY)
    img.append(images)

result = img[0]//15 + img[1]//15 + img[2]//15 + img[3]//15 + img[4]//15 + img[5]//15 + img[6]//15 + img[7]//15 + img[8]//15 + img[9]//15 + img[10]//15 + img[11]//15 + img[12]//15 + img[13]//15 + img[14]//15

cv2.imshow('output' , result)
cv2.imwrite('C:/Users/Hosein/Desktop/result.jpg',result)
cv2.waitKey()
