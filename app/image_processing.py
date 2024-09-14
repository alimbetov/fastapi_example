import cv2
import pytesseract
import numpy as np
from deepface import DeepFace
from fastapi import HTTPException

# Функция обработки изображения с использованием Tesseract
def process_image(image_path: str) -> str:
    # Загрузка изображения
    image = cv2.imread(image_path)

    # Преобразование изображения в градации серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Применение гауссовского размытия для уменьшения шумов
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Применение Tesseract для распознавания текста
    text = pytesseract.image_to_string(blurred, config='--psm 7')

    return text

# Функция для извлечения эмбеддингов с помощью DeepFace
def get_face_embedding(image: np.array):
    try:
        # Извлекаем эмбеддинги с использованием модели Facenet
        embedding = DeepFace.represent(img_path=image, model_name="Facenet", enforce_detection=False)[0]["embedding"]
        return embedding
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при получении эмбеддинга: {e}")
