import os
import shutil
import glob
import random

DATA_PATH = './dataset'
TARGET_PATH = './data/weather_dataset'
RATIO = 0.8

categories = ['cloudy', 'rain', 'shine', 'sunrise']

# Ensure the necessary subdirectories in the train and val folders
for split in ['train', 'val']:
    for category in categories:
        os.makedirs(os.path.join(TARGET_PATH, split, category), exist_ok=True)

# Sorting and moving images into their respective category folders
for category in categories:
    files = glob.glob(os.path.join(DATA_PATH, f'{category}*.jpg'))
    random.shuffle(files)

    split_point = int(len(files) * RATIO)
    train_files = files[:split_point]
    val_files = files[split_point:]

    for file in train_files:
        destination = os.path.join(TARGET_PATH, 'train', category, os.path.basename(file))
        shutil.move(file, destination)

    for file in val_files:
        destination = os.path.join(TARGET_PATH, 'val', category, os.path.basename(file))
        shutil.move(file, destination)