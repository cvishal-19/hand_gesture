# convert the image dataset into csv

import cv2
import mediapipe as mp
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

mp_holistic = mp.solutions.holistic
holistic_model = mp_holistic.Holistic(
    min_detection_confidence=0.24,
    min_tracking_confidence=0.24
)

mp_drawing = mp.solutions.drawing_utils

# data directory
data_dir = 'V:/Open cv/data'

df = pd.DataFrame()

def into_df(hand_landmarks, hand_type,k, label):
    if hand_landmarks:
        for idx, landmark in enumerate(hand_landmarks.landmark):
            landmark_name = mp_holistic.HandLandmark(idx).name
            
            column_name_x = str(hand_type) + "_" + str(landmark_name) + '_x'
            column_name_y = str(hand_type) + "_" + str(landmark_name) + '_y'
            column_name_z = str(hand_type) + "_" + str(landmark_name) + '_z'
            df.loc[k,'class'] = label
            df.loc[k,column_name_x] = landmark.x
            df.loc[k,column_name_y] = landmark.y
            df.loc[k,column_name_z] = landmark.z
               
k = 0

for classes in os.listdir(data_dir):
    for im in os.listdir(data_dir + '/' + str(classes)):
        img_path = data_dir + '/' + str(classes) + '/' + im
        # print(img_path)
        frame = cv2.imread(img_path)
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = holistic_model.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        into_df(results.left_hand_landmarks, "Left",k, classes)
        into_df(results.right_hand_landmarks, 'Right',k, classes)    
        k+=1
        
        

# img_path = 'V:/Open cv/WIN_20231203_19_56_49_Pro.jpg'
def print_landmark_info(hand_landmarks, hand_type):
    if hand_landmarks:
        for idx, landmark in enumerate(hand_landmarks.landmark):
            landmark_name = mp_holistic.HandLandmark(idx).name
            x, y, z = landmark.x, landmark.y, landmark.z
            
            print(f"{hand_type} Hand Landmark {landmark_name} - X: {x}, Y: {y}, Z: {z}")
            
print(f'here is your df: \n{df}')

df.to_csv("data_real.csv", index = True)

# frame = cv2.imread(img_path)

# # Convert the image to RGB format
# image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# image.flags.writeable = False
# results = holistic_model.process(image)
# image.flags.writeable = True

# print_landmark_info(results.right_hand_landmarks, "Right")
# print_landmark_info(results.left_hand_landmarks, "Left")

# mp_drawing.draw_landmarks(
#     image,
#     results.right_hand_landmarks,
#     mp_holistic.HAND_CONNECTIONS
# )

# mp_drawing.draw_landmarks(
#     image,
#     results.left_hand_landmarks,
#     mp_holistic.HAND_CONNECTIONS
# )

# plt.imshow( image)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
# plt.show()