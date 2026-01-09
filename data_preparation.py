import mediapipe as mp
import cv2 as cv
import time
from pathlib import Path
import numpy as np

path = Path("/Users/tosiachwala/Desktop/program/data/none/vid1.mov")
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


cap = cv.VideoCapture(path)
num_frames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
print(num_frames)
if not cap.isOpened():
    raise RuntimeError(f"Could not open video: {path}")
prev_frame_time = 0
new_frame_time = 0
num_of_videos = 0
frame_idx = 0

data = np.zeros((num_frames,21,3), dtype=np.float32)
try:

    while True:
        sucess, frame = cap.read()
        if not sucess or frame is None:
            print("end of video or cannot read frame")
            break
        #new_frame_time = time.time()
        imageRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        results = hands.process(imageRGB)
        #font = cv.FONT_HERSHEY_SIMPLEX
        #fps = 1/(new_frame_time-prev_frame_time)
        #prev_frame_time = new_frame_time
        #fps = int(fps)
        #fps = str(fps)
        #cv.putText(frame, fps, (50,100), font, 3, (100,255,0), 3, cv.LINE_AA)
        if results.multi_hand_landmarks:
            hand = results.multi_hand_world_landmarks[0]
            coords = np.array([[lm.x,lm.y,lm.z]for lm in hand.landmark], dtype=np.float32)

            """for handLms in results.multi_hand_landmarks:
                hand_id = hand_id + 1
                mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
                print(results.multi_hand_world_landmarks[0])
                """
        else :
            print(f"Frame {frame_idx}: hand detected? {bool(results.multi_hand_world_landmarks)}")

            if frame_idx > 0:
                coords = data[frame_idx - 1]
            else:  
                coords = np.zeros((21,3), dtype = np.float32)

        if frame_idx < num_frames:
            data[frame_idx] = coords
        frame_idx +=1
        #cv.imshow("Image", frame)
        #cv.waitKey(1)

    print(data)
    

finally:
    cap.release()
    cv.destroyAllWindows()
