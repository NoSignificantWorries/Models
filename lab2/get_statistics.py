import os
import mmcv
import numpy as np
import torch
from PIL import Image
from torchvision import transforms
from tqdm import tqdm


def calculate_mean_std(data_root, img_dirs):
    img_paths = []
    for img_dir in img_dirs:
        for filename in os.listdir(os.path.join(data_root, img_dir)):
            if filename.endswith((".jpg", ".jpeg", ".png", ".bmp")):
                img_paths.append(os.path.join(data_root, img_dir, filename))

    num_imgs = len(img_paths)
    if num_imgs == 0:
        raise ValueError(f"No images found in {os.path.join(data_root, img_dir)}")

    mean = torch.zeros(3)
    std = torch.zeros(3)
    pixel_count = 0

    transform = transforms.ToTensor()

    for img_path in tqdm(img_paths, desc="Calculating mean and std"):
        img = Image.open(img_path).convert("RGB")
        img_tensor = transform(img)
        
        num_pixels = img_tensor.size(1) * img_tensor.size(2)
        pixel_count += num_pixels

        mean += torch.sum(img_tensor, dim=[1, 2])
        std += torch.sum(img_tensor ** 2, dim=[1, 2])


    mean /= pixel_count
    std = torch.sqrt(std / pixel_count - mean ** 2)

    return mean.tolist(), std.tolist()


if __name__ == "__main__":
    data_root = "/home/dmitry/PythonProjects/datasets/toucan2/images"
    img_dirs = ["train", "test", "valid"]
    mean, std = calculate_mean_std(data_root, img_dirs)

    for i in range(len(mean)):
        mean[i] *= 255
        std[i] *= 255

    print(f"Mean: {mean}")
    print(f"Std: {std}")


