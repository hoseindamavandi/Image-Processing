import cv2

image1 = cv2.imread('/Users/hossein/Documents/python/Image-Processing/Level-1/be happy(rotate)/3.jpg')

image1 = cv2.rotate(image1, cv2.ROTATE_180)

cv2.imshow('show output',image1)
cv2.waitKey()
cv2.imwrite('output3.jpg', image1)