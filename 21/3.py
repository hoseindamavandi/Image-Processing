import cv2

if __name__ == '__main__' :
    image1=cv2.imread('3.jpg')

    image1=cv2.rotate(image1, cv2.ROTATE_180)

    cv2.imwrite('C:/Users/Hosein/Desktop/image3.jpg', image1)

    cv2.imshow('show output',image1)
    cv2.waitKey()