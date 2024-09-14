# app/controllers.py

from fastapi import APIRouter, UploadFile, File, HTTPException
from app.image_processing import process_image
from app.services import TestService
from app.entities.recognized_text import RecognizedText
import shutil
import os

router = APIRouter()

UPLOAD_DIRECTORY = "uploaded_images/"  # Директория для хранения загруженных изображений

# Создаем директорию для загрузки изображений, если ее еще нет
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

@router.post("/upload_image/")
async def upload_image(file: UploadFile = File(...)):
    try:
        # Сохраняем загруженный файл в директорию
        file_path = f"{UPLOAD_DIRECTORY}{file.filename}"
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Обрабатываем изображение и получаем распознанный текст
        return RecognizedText(recognized_text=process_image(file_path))
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




# Определяем эндпоинт
@router.get("/greet/{name}")
async def greet_user(name: str):
    # Используем сервис для обработки бизнес-логики
    greeting = TestService.get_greeting(name)

    return RecognizedText(recognized_text=greeting)
