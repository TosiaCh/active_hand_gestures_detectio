import numpy as np
import cv2 as cv
import mediapipe as mp
import glob
import os

#export to landmarks_raw.npz

root = "data"

classes = ["swipe_up","swipe_down","click","none"]
sequences = []
labels = []
hands = mp.solutions.hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.6,
            min_tracking_confidence=0.6
        )


for cls in classes:
    pattern = os.path.join(root, cls, "*.mov")
    video_files = glob.glob(pattern)
    

    for video in video_files:
        frames_list = []
        cap = cv.VideoCapture(video)
       

        while True:
            success, frame = cap.read()
            if not success or frame is None:
                break
            frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            results = hands.process(frame_rgb)
            if results.multi_hand_landmarks:
                hand_landmarks = results.multi_hand_landmarks[0]
                frame_vec = []
                for lm in hand_landmarks.landmark:
                    frame_vec.extend([lm.x, lm.y])
                frames_list.append(frame_vec)
        cap.release()
        
        if len(frames_list) == 0:
            continue
        seq = np.stack(frames_list)
        sequences.append(seq)
        labels.append(cls)
hands.close()


np.savez_compressed(
    "landmarks_raw.npz",
    sequences=np.array(sequences, dtype=object),
    labels=np.array(labels, dtype=object),
)


#test loading
data = np.load("landmarks_raw.npz", allow_pickle=True)
seqs = data["sequences"]
labs = data["labels"]

print("N:", len(seqs))
print("First:", seqs[0].shape, labs[0])
print("Min/Max length:", min(s.shape[0] for s in seqs), max(s.shape[0] for s in seqs))
