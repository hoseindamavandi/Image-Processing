import cv2
import cvzone

back = cv2.imread('/Users/hossein/Documents/python/Image-Processing/Level-4/face filter/install git with brew.png',0)
front = cv2.imread('/Users/hossein/Documents/python/Image-Processing/Level-4/face filter/emojis/emoji1.png',0)
print(back.shape)
front = cv2.resize(front,(20,20))
result = cvzone.overlayPNG(back , front , [100,100])

cv2.imshow('test',result)
cv2,cv2.waitKey(0)