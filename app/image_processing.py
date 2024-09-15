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

# Функция для извлечения эмбеддингов с использованием DeepFace
def get_face_embedding(image: np.array, inIsDeep: bool = False, inEnforceFaceDetection: bool = False):
    try:
        # Выбираем модель в зависимости от значения inIsDeep
        inModelName = "Facenet512" if inIsDeep else "Facenet"
        
        # Преобразуем изображение в формат, поддерживаемый DeepFace
        embedding = DeepFace.represent(img_path=image, model_name=inModelName, enforce_detection=inEnforceFaceDetection)[0]["embedding"]
        
        return embedding
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при получении эмбеддинга: {e}")


    # Словарь для отображения типа классификатора на соответствующий XML файл
CLASSIFIER_FILES = {
    "eye": "haarcascade_eye.xml",
    "eyeglasses": "haarcascade_eye_tree_eyeglasses.xml",
    "catface": "haarcascade_frontalcatface.xml",
    "catface_extended": "haarcascade_frontalcatface_extended.xml",
    "frontalface_alt": "haarcascade_frontalface_alt.xml",
    "frontalface_alt2": "haarcascade_frontalface_alt2.xml",
    "frontalface_alt_tree": "haarcascade_frontalface_alt_tree.xml",
    "frontalface_default": "haarcascade_frontalface_default.xml",
    "fullbody": "haarcascade_fullbody.xml",
    "lefteye": "haarcascade_lefteye_2splits.xml",
    "license_plate": "haarcascade_license_plate_rus_16stages.xml",
    "lowerbody": "haarcascade_lowerbody.xml",
    "profileface": "haarcascade_profileface.xml",
    "righteye": "haarcascade_righteye_2splits.xml",
    "russian_plate": "haarcascade_russian_plate_number.xml",
    "smile": "haarcascade_smile.xml",
    "upperbody": "haarcascade_upperbody.xml"
}

def detect_faces(image: np.array, classifier_type: str) -> np.array:
    try:
        # Проверяем, что переданный тип классификатора существует
        if classifier_type not in CLASSIFIER_FILES:
            raise HTTPException(status_code=400, detail=f"Неизвестный тип классификатора: {classifier_type}")
        
        # Загрузка классификатора
        classifier_file = CLASSIFIER_FILES[classifier_type]
        classifier_path = cv2.data.haarcascades + 'app/haarcascades/' + classifier_file
        face_cascade = cv2.CascadeClassifier(classifier_path)
        
        # Преобразование изображения в серый цвет для детектирования лиц
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Обнаружение лиц на изображении
        faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        return faces
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при обнаружении лиц: {e}")