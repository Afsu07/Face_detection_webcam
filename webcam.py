import cv2


video = cv2.VideoCapture(0)


while True:
    
    succes,frame = video.read()
    grey_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # face
    face_cascade = cv2.CascadeClassifier('D:\DL_project\data\haarcascade_frontalface_default.xml')
    # eyes
    eyes_cascade = cv2.CascadeClassifier('D:\DL_project\data\haarcascade_eye.xml')
    faces = face_cascade.detectMultiScale(grey_img,scaleFactor=1.1,minNeighbors = 4, minSize = (30,30))
    eyes = eyes_cascade.detectMultiScale(grey_img,scaleFactor=1.1,minNeighbors = 4, minSize = (30,30))
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,pt1=(x,y), pt2=(x+w,y+h), color=(0,255,0), thickness=2)
    
    for (x,y,w,h) in eyes:
        cv2.rectangle(frame,pt1=(x,y), pt2=(x+w,y+h), color=(255,0,0), thickness=2)
    
    cv2.imshow('video',frame)
    if cv2.waitKey(1) & 0XFF == 27:
        break
video.release
cv2.destroyAllWindows()    
