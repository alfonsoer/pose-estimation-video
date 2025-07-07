# -*- coding: utf-8 -*-
"""
Automatically estimate human poses (2D skeleton) in a video with one or two people, 
using a pre-trained model and visualizing the result with annotations over the video

Alfonso ESTUDILLO ROMERO, 07/07/2025
"""

# import cv2
# import mediapipe as mp

# # Pose init
# mp_pose = mp.solutions.pose
# pose = mp_pose.Pose(static_image_mode=False)
# mp_drawing = mp.solutions.drawing_utils

# # Video load
# cap = cv2.VideoCapture("input/TimaMiroshnichenko.mp4")
# width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = cap.get(cv2.CAP_PROP_FPS)

# # Save outpit video
# out = cv2.VideoWriter("output/annotated_video.mp4",
#                       cv2.VideoWriter_fourcc(*'mp4v'),
#                       fps, (width, height))

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Convert to RGB
#     frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     results = pose.process(frame_rgb)

#     # If known poses, then draw them
#     if results.pose_landmarks:
#         mp_drawing.draw_landmarks(
#             frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

#     out.write(frame)

# cap.release()
# out.release()
# print("Finished: 'output/annotated_TimaMiroshnichenko.mp4'")

from ultralytics import YOLO
import cv2

#Load pretrained YOLO
model = YOLO("yolov8n-pose.pt")

#Video load
cap = cv2.VideoCapture("input/cottonbro_studio.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#Scale the output
scale = 0.50
new_width = int(width * scale)
new_height = int(height * scale)

#Save outpit video
out = cv2.VideoWriter("output/annotated_cottonbro_studio.mp4", 
                      cv2.VideoWriter_fourcc(*'mp4v'), 
                      fps, (new_width, new_height))

# Keypoints COCO to be anotated
KEYPOINT_NAMES = {
    0: "Nose",
    1: "Left Eye",
    2: "Right Eye",
    5: "Left Shoulder",
    6: "Right Shoulder"
}
frame_count = 0
# max_frames = 224  # ← Número máximo de frames a procesar


while cap.isOpened()  :
    ret, frame = cap.read()
    if not ret:
        break
    
    frame_count += 1  # ← Incrementa el contador
    
    #Inference with YOLOv8-Pose
    results = model(frame)
    annotated_frame = results[0].plot()

    for kp in results[0].keypoints:
        for i, (x, y, conf) in enumerate(kp.data[0]):  # Solo primer frame
            if i in KEYPOINT_NAMES and conf > 0.5:
                #Anotation
                label = KEYPOINT_NAMES[i]
                cv2.putText(
                    annotated_frame,
                    label,
                    (int(x), int(y) - 10),                # Posición más alta para que no tape el punto
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.5,                                  # tamaño del texto  
                    (0, 255, 0),                          # color verde
                    2,                                    #grosor de línea 
                    cv2.LINE_AA
                )
    resized_frame = cv2.resize(annotated_frame, (new_width, new_height), interpolation=cv2.INTER_AREA)
    out.write(resized_frame)

cap.release()
out.release()