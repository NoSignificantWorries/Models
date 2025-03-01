from ultralytics import YOLO
import torch
import os

model = YOLO('runs/detect/train12/weights/epoch190.pt')

path = "../datasets/toucan/train/images"
for file in os.listdir(path):
    print(file)
    results = model.predict(f"{path}/{file}", imgsz=640, save=True)

