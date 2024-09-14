# app/image_processing.py

import cv2
import pytesseract
from PIL import Image
import numpy as np
import shutil
import os

DIR_FOR_UNPROCESSED_IMAGES = "/unprocessed/"

# Функция обработки изображения с использованием Tesseract
def process_image(image_path: str) -> str:
    # Загрузка изображения
    image = cv2.imread(image_path)

    # Преобразование изображения в градации серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    convertMatrixIntoImageThenSave(f'{image_path}_gray_scale', matrix=gray)

    # Применение гауссовского размытия для уменьшения шумов
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    convertMatrixIntoImageThenSave(f'{image_path}_blur', matrix=blurred)

    # Применение Tesseract для распознавания текста
    text = pytesseract.image_to_string(blurred, config='--psm 7')

    return text


def convertMatrixIntoImageThenSave(orginal_file_path, matrix):
    file_directory = os.path.dirname(orginal_file_path)
    filename = os.path.basename(orginal_file_path)

    if not os.path.exists(f'{file_directory}{DIR_FOR_UNPROCESSED_IMAGES}'):
        os.makedirs(f'{file_directory}{DIR_FOR_UNPROCESSED_IMAGES}')

    file_path = f"{file_directory}{DIR_FOR_UNPROCESSED_IMAGES}{filename}.png"

    # Save the matrix as an image
    if (cv2.imwrite(file_path, matrix) == True):
        print(f'{file_path} is saved')
    else:
        print(f'{file_path} is not saved')