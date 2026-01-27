import os
import cv2
import numpy as np
from utils import get_face_landmarks

data_dir = './data/processed_data'
output = []

for emotion_indx, emotion in enumerate(os.listdir(data_dir)):
    emotion_path = os.path.join(data_dir, emotion)

    # macOS .DS_Store ve dosyaları atla
    if not os.path.isdir(emotion_path):
        continue

    for image_name in os.listdir(emotion_path):
        image_path = os.path.join(emotion_path, image_name)

        image = cv2.imread(image_path)
        if image is None:
            continue

        face_landmarks = get_face_landmarks(image)
        if face_landmarks is None:
            continue

        if len(face_landmarks) == 1404:
            row = face_landmarks.copy()
            row.append(emotion_indx)
            output.append(row)

output = np.asarray(output, dtype=np.float32)
np.savetxt('data.txt', output)

print("Bitti. Üretilen örnek sayısı:", output.shape[0])
print("Feature boyutu:", output.shape[1])
