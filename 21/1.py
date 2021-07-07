import cv2
import numpy as np

if __name__ == '__main__' :
    imgboard=np.zeros((800,800))

    for i in range(800):
        for j in range(800):
            if (i//100)%2==0:
                if (j//100)%2==0:
                    imgboard[i,j]=0
                elif (j//100)%2!=0:
                    imgboard[i,j]=255
            elif (i//100)%2!=0:
                if (j//100)%2==0:
                    imgboard[i,j]=255
                elif (j//100)%2!=0:
                    imgboard[i,j]=0
    cv2.imwrite('C:/Users/Hosein/Desktop/img.jpg' , imgboard)
    cv2.imshow('show outpuyt',imgboard)
    cv2.waitKey()



