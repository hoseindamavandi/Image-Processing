import cv2

image = []
images = []
img_result = []

for j in range(1, 5):
    for i in range(1, 6):
        img = cv2.imread(f'black hole/{j}/{i}.jpg')
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        image.append(img)
    img_result = image[j] // 5 + image[1] // 5 + image[2] // 5 + image[3] // 5 + image[4] // 5
    image=[]
    images.append(img_result)


result = cv2.vconcat([
    cv2.hconcat([images[0], images[1]]),
    cv2.hconcat([images[2], images[3]])
])

cv2.imwrite('C:/Users/Hosein/Desktop/image.jpg', result)
cv2.imshow('result', result)
cv2.waitKey()
