# app/controllers.py
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.image_processing import process_image, get_face_embedding
import shutil
import os

router = APIRouter()

UPLOAD_DIRECTORY = "uploaded_images/"  # Директория для хранения загруженных изображений

# Создаем директорию для загрузки изображений, если ее еще нет
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

@router.post("/img-ocr/")
async def upload_image(file: UploadFile = File(...)):
    try:
        # Сохраняем загруженный файл в директорию
        file_path = f"{UPLOAD_DIRECTORY}{file.filename}"
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Обрабатываем изображение и получаем распознанный текст
        recognized_text = process_image(file_path)
        return {"text": recognized_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Маршрут для загрузки изображения и получения эмбеддингов
@app.post("/face_embedding/")
async def get_embedding(file: UploadFile = File(...)):
    try:
        # Открываем изображение и конвертируем его в формат, пригодный для обработки
        image = Image.open(io.BytesIO(await file.read()))
        image = np.array(image)

        # Проверяем, является ли файл изображением
        if not image.shape or len(image.shape) != 3: 
            raise HTTPException(status_code=400, detail="Загруженный файл не является изображением.")

        # Получаем эмбеддинги
        embedding = get_face_embedding(image)

        return {"embedding": embedding}
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code = 400, detail = f"Не удалось обработать изображение: {e}")


# Определяем эндпоинт
@router.get("/greet/{name}")
async def greet_user(name: str):
    # Используем сервис для обработки бизнес-логики
    greeting = TestService.get_greeting(name)
    return {"message": greeting}
