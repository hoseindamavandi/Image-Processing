import cv2
import  numpy as np

video_cap = cv2.VideoCapture(0)

while 1:
    ret , frame = video_cap.read()

    if not ret:
        break

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    target = frame[200:300,300:400]

    kernel = np.ones((45,45))/2025

    frame = cv2.filter2D(frame, -1 , kernel)

    frame[200:300,300:400] = target

    cv2.rectangle(frame, (300,200) , (400,300), (0,0,0), 4)

    if np.average(target) < 50:
        cv2.putText(frame, "Black", (10,30) , cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0))
    elif np.average(target) < 170:
        cv2.putText(frame, "Gray", (10,30) , cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0))
    else:
        cv2.putText(frame, "White", (10,30) , cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0))

    cv2.imshow("result", frame)
    if cv2.waitKey(1) == ord('q'):
        break