import os
import hashlib
import numpy as np
from PIL import Image
from fastapi import APIRouter, UploadFile, File, HTTPException
from .image_processing import process_image, get_face_embedding, detect_faces

router = APIRouter()

UPLOAD_DIRECTORY = "uploaded_images/"
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

def remove_file(file_path: str):
    if os.path.isfile(file_path):
        os.remove(file_path)

def save_file(file: UploadFile):
    file_extension = os.path.splitext(file.filename)[1]  # Get file extension
    
    # Generate a hash of the file content for uniqueness
    file_content = file.file.read()  # Read file content
    file_hash = hashlib.sha256(file_content).hexdigest()
    
    unique_filename = f"{file_hash}{file_extension}"  # Create a unique file name
    file_path = os.path.join(UPLOAD_DIRECTORY, unique_filename)
    
    # Save the file
    with open(file_path, "wb") as f:
        f.write(file_content)  # Write file content
    
    # Return the file path
    return file_path

@router.post("/img-ocr/")
async def upload_image(file: UploadFile = File(...)):
    try:
        file_path = save_file(file)
        recognized_text = process_image(file_path)
        return {"text": recognized_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        remove_file(file_path)

@router.post("/face_embedding/")
async def get_embedding(file: UploadFile = File(...), inIsDeep: bool = False, inEnforceFaceDetection: bool = False):
    try:
        file_path = save_file(file)
        image = Image.open(file_path)
        image = np.array(image)

        if len(image.shape) != 3:
            raise HTTPException(status_code=400, detail="Uploaded file is not an image.")

        embedding = get_face_embedding(image, inIsDeep=inIsDeep, inEnforceFaceDetection=inEnforceFaceDetection)
        return {"embedding": embedding}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to process image: {e}")
    finally:
        remove_file(file_path)

@router.post("/detect_faces/")
async def detect_faces_route(file: UploadFile = File(...), classifier_type: str = 'frontalface_default'):
    try:
        file_path = save_file(file)
        image = Image.open(file_path)
        image = np.array(image)

        if len(image.shape) != 3:
            raise HTTPException(status_code=400, detail="Uploaded file is not an image.")

        faces = detect_faces(image, classifier_type)
        return {"faces": faces.tolist()}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to process image: {e}")
    finally:
        remove_file(file_path)
