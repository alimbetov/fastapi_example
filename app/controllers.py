import io
import os
import shutil
import numpy as np
from PIL import Image
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.image_processing import process_image, get_face_embedding, detect_faces

router = APIRouter()

UPLOAD_DIRECTORY = "uploaded_images/"
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

def remove_file(file_path: str):
    if os.path.isfile(file_path):
        os.remove(file_path)

@router.post("/img-ocr/")
async def upload_image(file: UploadFile = File(...)):
    file_path = f"{UPLOAD_DIRECTORY}{file.filename}"
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        recognized_text = process_image(file_path)
        return {"text": recognized_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        remove_file(file_path)

@router.post("/face_embedding/")
async def get_embedding(file: UploadFile = File(...), inIsDeep: bool = False, inEnforceFaceDetection: bool = False):
    file_path = f"{UPLOAD_DIRECTORY}{file.filename}"
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        image = Image.open(file_path)
        image = np.array(image)

        if image is None or len(image.shape) != 3:
            raise HTTPException(status_code=400, detail="Загруженный файл не является изображением.")

        embedding = get_face_embedding(image, inIsDeep=inIsDeep, inEnforceFaceDetection=inEnforceFaceDetection)
        return {"embedding": embedding}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Не удалось обработать изображение: {e}")
    finally:
        remove_file(file_path)

@router.post("/detect_faces/")
async def detect_faces_route(file: UploadFile = File(...), classifier_type: str = 'frontalface_default'):
    file_path = f"{UPLOAD_DIRECTORY}{file.filename}"
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        image = Image.open(file_path)
        image = np.array(image)

        if len(image.shape) != 3:
            raise HTTPException(status_code=400, detail="Загруженный файл не является изображением.")

        faces = detect_faces(image, classifier_type)
        return {"faces": faces.tolist()}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Не удалось обработать изображение: {e}")
    finally:
        remove_file(file_path)
