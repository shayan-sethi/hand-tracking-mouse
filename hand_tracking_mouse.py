import cv2
import mediapipe as mp
import pyautogui
import time
import math

capturedhands = mp.solutions.hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
drawing = mp.solutions.drawing_utils
cam = cv2.VideoCapture(0)
screenwidth, screenheight = pyautogui.size()

x1 = y1 = x2 = y2 = 0

while True:
    success, image = cam.read()
    if not success:
        continue

    image = cv2.flip(image, 1)
    imageheight, imagewidth, _ = image.shape
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = capturedhands.process(rgb_image)

    hands = results.multi_hand_landmarks if results else None

    if hands:
        for hand in hands:
            drawing.draw_landmarks(image, hand, mp.solutions.hands.HAND_CONNECTIONS)
            onehand = hand.landmark
            for id, lm in enumerate(onehand):
                x = int(lm.x * imagewidth)
                y = int(lm.y * imageheight)

                if id == 8:
                    mouse_x = int(screenwidth / imagewidth * x)
                    mouse_y = int(screenheight / imageheight * y)
                    pyautogui.moveTo(mouse_x, mouse_y)

                    x1 = x
                    y1 = y
                    cv2.circle(image, (x, y), 10, (0, 255, 255), -1)

                if id == 4:
                    cv2.circle(image, (x, y), 10, (0, 255, 255), -1)
                    x2 = x
                    y2 = y

        dist = math.hypot(x2 - x1, y2 - y1)
        if dist < 40:
            pyautogui.click()
            time.sleep(0.2)

    cv2.imshow("hand", image)
    key = cv2.waitKey(1)
    if key == 27:
        break

    time.sleep(0.01)

cam.release()
cv2.destroyAllWindows()

