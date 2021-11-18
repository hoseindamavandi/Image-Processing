import cv2
import cvzone

face_detector = cv2.CascadeClassifier('/Users/hossein/Documents/python/Image-Processing/Level-4/face filter/haarcascades/haarcascade_frontalface_default.xml')
eyes_detector = cv2.CascadeClassifier('/Users/hossein/Documents/python/Image-Processing/Level-4/face filter/haarcascades/haarcascade_eye.xml')
lips_detector = cv2.CascadeClassifier('/Users/hossein/Documents/python/Image-Processing/Level-4/face filter/haarcascades/haarcascade_smile.xml')

face_emoji = cv2.imread('/Users/hossein/Documents/python/Image-Processing/Level-4/face filter/emojis/emoji1.png',cv2.IMREAD_UNCHANGED)
eyes_emoji = cv2.imread('/Users/hossein/Documents/python/Image-Processing/Level-4/face filter/emojis/eyes.png',cv2.IMREAD_UNCHANGED)
lips_emoji = cv2.imread('/Users/hossein/Documents/python/Image-Processing/Level-4/face filter/emojis/lips.png',cv2.IMREAD_UNCHANGED)

flag = 0

def change_face(frame,f):

    faces = face_detector.detectMultiScale(frame , 1.3)

    for (x , y , w , h) in faces:
        emoji_resized = cv2.resize(face_emoji , (w,h))
        
        #frame[y:y+h,x:x+w] = emoji_resized
        frame = cvzone.overlayPNG(frame, emoji_resized, [x,y])
        
    f = 1

    return frame,f


def change_eyes(frame,f):

    faces = eyes_detector.detectMultiScale(frame , 1.1, minSize=(20,20),maxSize=(25,25))

    for (x , y , w , h) in faces:
        emoji_resized = cv2.resize(eyes_emoji , (w,h))
        
        #frame[y:y+h,x:x+w] = emoji_resized
        frame = cvzone.overlayPNG(frame, emoji_resized, [x,y])
        
    f = 2

    return frame,f

def change_lips(frame,f):

    faces = lips_detector.detectMultiScale(frame , 1.34, 29)

    for (x , y , w , h) in faces:
        emoji_resized = cv2.resize(lips_emoji , (w,h))
        
        #frame[y:y+h,x:x+w] = emoji_resized
        frame = cvzone.overlayPNG(frame, emoji_resized, [x,y])
        
    f = 3

    return frame,f


def blur_face(frame,f):

    faces = face_detector.detectMultiScale(frame , 1.2)

    for (x , y , w , h) in faces:

        image_blur = frame[y:y+h,x:x+w]
        
        #emoji_resized = cv2.resize(lips_emoji , (w,h))
        image_blur = cv2.resize(image_blur,(int(w//20),int(h//20)))
        image_blur = cv2.resize(image_blur,(w,h))
        frame[y:y+h,x:x+w] = image_blur
        
    f = 4

    return frame,f

vedio_cap = cv2.VideoCapture(0)

while 1:

    ret , frame = vedio_cap.read()

    if ret == False:
        break

    frame = cv2.resize(frame, (0, 0), fx=0.25 , fy=0.25)

    key = cv2.waitKey(1)
    if key == ord('0'):
        flag = 0
    if key == ord('5'):
        break
    if key == ord('1') or flag == 1:
        frame,flag = change_face(frame, flag)
    if key == ord('2') or flag == 2:
        frame, flag = change_eyes(frame, flag)
    if key == ord('3') or flag == 3:
        frame, flag = change_lips(frame, flag)
    if key == ord('4') or flag == 4:
        frame, flag = blur_face(frame, flag)
    
    cv2.imshow('output', frame)
    #cv2.waitKey(10)
    









