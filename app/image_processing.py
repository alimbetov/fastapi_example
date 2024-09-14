# app/image_processing.py

import cv2
import pytesseract
from PIL import Image
import numpy as np
import shutil
import os

DIR_FOR_UNPROCESSED_IMAGES = "/unprocessed/"
UPLOAD_DIRECTORY = "uploaded_images/" 

if not os.path.exists(f'{UPLOAD_DIRECTORY}{DIR_FOR_UNPROCESSED_IMAGES}'):
        os.makedirs(f'{UPLOAD_DIRECTORY}{DIR_FOR_UNPROCESSED_IMAGES}')


# Функция обработки изображения с использованием Tesseract
def process_image(image_path: str) -> str:
    # Загрузка изображения
    image = cv2.imread(image_path)

    # Преобразование изображения в градации серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    convertMatrixIntoImageThenSave(get_filename_for_image(image_path, '_gray_scale'), matrix=gray)

    # _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # cv2.drawContours(gray, contours, -1, (0, 255, 0), 2)
    # convertMatrixIntoImageThenSave(get_filename_for_image(image_path, '_contour'), matrix=gray)

    # # Применение гауссовского размытия для уменьшения шумов
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    convertMatrixIntoImageThenSave(get_filename_for_image(image_path, '_blur'), matrix=blurred)


    # Применение Tesseract для распознавания текста
    text = pytesseract.image_to_string(blurred, config='--psm 7')

    return text


def convertMatrixIntoImageThenSave(filepath, matrix):
    # Save the matrix as an image
    if (cv2.imwrite(filepath, matrix) == True):
        print(f'{filepath} is saved')
    else:
        print(f'{filepath} is not saved')


def get_filename_for_image(orginal_file_path, image_type):
    file_directory = os.path.dirname(orginal_file_path)
    filename = os.path.basename(orginal_file_path)
    clean_filename, _ = os.path.splitext(filename)

    return f"{file_directory}{DIR_FOR_UNPROCESSED_IMAGES}{clean_filename}{image_type}.png"
