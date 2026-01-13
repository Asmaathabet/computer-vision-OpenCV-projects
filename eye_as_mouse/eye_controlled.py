# eye controlled mouse using eye tracking
import cv2
import mediapipe
import pyautogui

cam = cv2.VideoCapture(0)
while True:
    _, frame = cam.read()
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_mesh = mediapipe.solutions.face_mesh.FaceMesh()
    result = face_mesh.process(frame_rgb)
    # print(result.multi_face_landmarks)

    if result.multi_face_landmarks:
        landmarks = result.multi_face_landmarks[0].landmark

        for landmark in landmarks: # landmark = each point of face
            left_eye_x = int(landmarks[159].x * frame.shape[1]) # 159 is the index for left eye
            left_eye_y = int(landmarks[159].y * frame.shape[0]) # 159 is the index for left eye
            cv2.circle(frame, (left_eye_x, left_eye_y), 5, (0, 255, 0), -1)

        screen_width, screen_height = pyautogui.size()
        mouse_x = int((left_eye_x / frame.shape[1]) * screen_width)
        mouse_y = int((left_eye_y / frame.shape[0]) * screen_height)

        pyautogui.moveTo(mouse_x, mouse_y)

    cv2.imshow("Eye Controlled Mouse", frame)
    key = cv2.waitKey(10)
    if key == 27:  # Escape key
        break
cam.release()
cv2.destroyAllWindows()
