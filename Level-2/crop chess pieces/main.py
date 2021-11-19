import cv2

img = cv2.imread('chess pieces.jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
print(img.shape)
for i in range(7):
    a = img[0:275,i*83:83+i*83]
    cv2.imwrite(f'chesspieces{i}.jpg',a)
