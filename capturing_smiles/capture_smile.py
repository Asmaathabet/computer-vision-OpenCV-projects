# Capturing smile face
import cv2
import mediapipe
import pyautogui
import winsound

x1,x2,y1,y2 = 0,0,0,0
face_mesh = mediapipe.solutions.face_mesh.FaceMesh(refine_landmarks=True)
cam = cv2.VideoCapture(0)

while True:
    _, image = cam.read()
    image = cv2.flip(image, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(image_rgb)
    landmarks_pts = output.multi_face_landmarks
    
    if landmarks_pts:
        landmarks = landmarks_pts[0].landmark
        for id, landmark in enumerate(landmarks):
            # print(landmark.x, landmark.y)
            x = int(landmark.x * image.shape[1])
            y = int(landmark.y * image.shape[0])
            if id == 43: 
                x1,y1 = x,y
            if id == 287: 
                x2,y2 = x,y
            # print(x,y)
        distance = int(((x2 - x1)**2 + (y2 - y1)**2 )**(0.5))
        print(distance)
        if distance > 70:  # Adjust threshold as needed
            # cv2.imwrite(f"smile_{distance}.png", image)
            print("Smiling")
            winsound.Beep(2500, 500)  # Beep sound for 0.5 second
            cv2.waitKey(200)  # Wait to avoid multiple beeps

    cv2.imshow("Capturing Smile Faces", image)
    key = cv2.waitKey(10)
    if key == 27:  # Escape key
        break

cam.release()
cv2.destroyAllWindows()

