import cv2
# print(cv2.__version__)

# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

webcam = cv2.VideoCapture(0)
while True:
    _,img = webcam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2 , 4)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y), (x+w, y+h), (0,0,255), 4)  
    cv2.imshow("Face detection", img)
    key = cv2.waitKey(10)
    # 27 --> escape
    if key == 27:
        break
webcam.release()
cv2.destroyAllWindows()



