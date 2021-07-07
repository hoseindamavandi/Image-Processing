import cv2

img1 = cv2.imread('board-origin.bmp')
imgtest = cv2.flip(cv2.imread('board-test.bmp'), 1)

img1 = cv2.cvtColor(img1,cv2.COLOR_RGB2GRAY)
imgtest = cv2.cvtColor(imgtest,cv2.COLOR_RGB2GRAY)

result =  cv2.subtract(imgtest,img1)
result=result*2
cv2.imwrite('C:/Users/Hosein/Desktop/orgin.bmp',result)
cv2.imshow('output', result)
cv2.waitKey()