import cv2

if __name__ == '__main__' :
    image=cv2.imread('4.jpg')
    image=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)


    rows=image.shape[0]
    cols=image.shape[1]

    for i in range(rows):
        for j in range(cols):
            if image[i,j]>40:
                image[i,j]=255
            else:
                image[i,j]=0

    cv2.imshow('show output', image)
    cv2.waitKey()
    cv2.imwrite('C:/Users/Hosein/Desktop/image.jpg',image)
