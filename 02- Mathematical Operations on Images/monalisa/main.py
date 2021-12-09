import cv2
import numpy as np

image = cv2.imread('Mona_Lisa.jpg')
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
cols = image.shape[0]
rows = image.shape[1]
mask = np.tile(np.linspace(10, 200, rows), (cols, 1))

mask = np.uint8(mask)

result = (image / mask)
cv2.imwrite('C:/Users/Hosein/Desktop/result.jpg',result)
cv2.imshow('output',result)
cv2.waitKey()
