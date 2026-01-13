# Build a home Security Camera 
import cv2
import winsound

webcam = cv2.VideoCapture(0)
while True:
    _,image1 = webcam.read()
    _,image2 = webcam.read()
    diff = cv2.absdiff(image1, image2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    
    _,thresh = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  
    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        winsound.Beep(2500, 1000)  # Beep sound for 1 second
        # winsound.Beep(500, 100) # Lower pitch beep for 0.1 second

    cv2.imshow("Security Camera", gray)

    if cv2.waitKey(10) == 27:  # Escape key
        break
webcam.release()
cv2.destroyAllWindows()
