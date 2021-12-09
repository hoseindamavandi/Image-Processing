import cv2

image1 = cv2.imread('1.jpg')
image2 = cv2.imread('2.jpg')

image1 = 255 - image1
image2 = 255 - image2

cv2.imwrite('C:/Users/Hosein/Desktop/image1.jpg',image1)
cv2.imwrite('C:/Users/Hosein/Desktop/image2.jpg',image2)

cv2.imshow('show output', image1)
cv2.waitKey()
cv2.imshow('show output', image2)
cv2.waitKey()



