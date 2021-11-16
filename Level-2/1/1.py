import cv2

a=cv2.imread('a.tif')
b=cv2.imread('b.tif')

a=cv2.cvtColor(a,cv2.COLOR_BGR2RGB)
b=cv2.cvtColor(b,cv2.COLOR_BGR2RGB)

secret= b-a

cv2.imshow('output',secret)
cv2.waitKey()
