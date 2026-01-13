# hand gesture volume control 
import cv2
import mediapipe as mp
import pyautogui

x1,y1,x2,y2 = 0,0,0,0

webcam = cv2.VideoCapture(0)
my_hand = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

key = None
while True:
    _, image = webcam.read()
    image = cv2.flip(image, 1)
    frame_height, frame_width, _ = image.shape
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output = my_hand.process(rgb_image)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(image, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                # print(id, x, y)
                if id == 4:
                    x1, y1 = x, y
                    cv2.circle(image, (x1, y1), 10, (0, 255, 0), cv2.FILLED)
                if id == 8:
                    x2, y2 = x, y
                    cv2.circle(image, (x2, y2), 10, (0, 255, 0), cv2.FILLED)
            
            length = (((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
            cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 3)
            # print(length)
            if length > 50:
                # cv2.circle(image, ((x1 + x2) // 2, (y1 + y2) // 2), 10, (255, 0, 255), cv2.FILLED)
                pyautogui.press("volumeup")
            else:
                pyautogui.press("volumedown")


    cv2.imshow("Hand Volume control using python", image)
    
    key = cv2.waitKey(10)
    # 27 --> escape
    if key == 27:
        break
webcam.release()
cv2.destroyAllWindows()

