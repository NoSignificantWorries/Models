from ultralytics import YOLO
import torch

model = YOLO('yolov8s.pt')
'''
for name, param in model.named_parameters():
    print(name)'''
results = model.train(data='../datasets/toucan/data.yaml', epochs=300, imgsz=640, freeze=[0, 1, 2, 3, 4])
# results = model.predict(source='../datasets/toucan/train/images/1007_jpg.rf.6bc11d8e07612d92fcd1bfb9a2ea284f.jpg', imgsz=640)

# print(results)

