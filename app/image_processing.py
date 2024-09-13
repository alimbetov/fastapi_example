# app/image_processing.py

import cv2
import pytesseract
from PIL import Image
import numpy as np

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
