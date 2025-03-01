from ultralytics import YOLO
import torch

model = YOLO('yolov8s.pt')

n = len(list(model.named_parameters()))
print(n)
for i, (name, param) in enumerate(model.named_parameters()):
    if i <= n - 4:
        param.requires_grad = False
results = model.train(data='../datasets/toucan/data.yaml', epochs=300, imgsz=640, batch=4, save_period=10)

