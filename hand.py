import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture(0, cv.CAP_AVFOUNDATION)
num_frames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
prev_frame_time = 0
new_frame_time = 0
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


while True:
    sucess, frame = cap.read()
    new_frame_time = time.time()
    imageRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = hands.process(imageRGB)
    
    font = cv.FONT_HERSHEY_SIMPLEX
    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time
    fps = int(fps)
    fps = str(fps)
    cv.putText(frame, fps, (50,100), font, 3, (100,255,0), 3, cv.LINE_AA)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)


    cv.imshow("Image", frame)
    cv.waitKey(1)