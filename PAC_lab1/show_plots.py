import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из results.csv
data = pd.read_csv('runs/detect/train6/results.csv') #  Укажите правильный путь

# Вывод первых строк данных
print(data.head())

# График потерь
plt.figure(figsize=(12, 6))
plt.plot(data['train/box_loss'], label='Box Loss')
plt.plot(data['train/cls_loss'], label='Class Loss')
plt.plot(data['train/dfl_loss'], label='DFL Loss')
plt.xlabel('Эпоха')
plt.ylabel('Потери')
plt.title('График Потерь')
plt.legend()
plt.show()

# График mAP
plt.figure(figsize=(12, 6))
plt.plot(data['metrics/mAP50(B)'], label='mAP@0.5')
plt.plot(data['metrics/mAP50-95(B)'], label='mAP@0.5:0.95')
plt.xlabel('Эпоха')
plt.ylabel('mAP')
plt.title('График mAP')
plt.legend()
plt.show()

