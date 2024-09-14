# FastAPI Example Project

# FastAPI Image Processing Service

This project is a FastAPI-based web service designed for image processing tasks, including Optical Character Recognition (OCR) and face embedding extraction.

## Features

1. **Create Directory for Image Uploads**:
   - Automatically creates a directory for storing uploaded images if it does not already exist.

2. **OCR (Optical Character Recognition)**:
   - **Endpoint**: `/img-ocr/`
   - **Method**: `POST`
   - **Description**: Upload an image to this endpoint to extract text from it using Tesseract OCR. The image is saved to a specified directory before processing.
   - **Request**: Upload an image file.
   - **Response**: Returns the recognized text extracted from the image.

3. **Face Embedding Extraction**:
   - **Endpoint**: `/face_embedding/`
   - **Method**: `POST`
   - **Description**: Upload an image to this endpoint to extract face embeddings using DeepFace. The image is processed directly from the file upload.
   - **Request**: Upload an image file.
   - **Response**: Returns the face embedding vector of the uploaded image.

4. **Greeting Endpoint**:
   - **Endpoint**: `/greet/{name}`
   - **Method**: `GET`
   - **Description**: Provides a greeting message for the provided name.
   - **Request**: Pass the name as a path parameter.
   - **Response**: Returns a greeting message.

#### POST /detect_faces/
Загружает изображение и обнаруживает лица на основе указанного типа классификатора.
**Параметры запроса:**
- `file`: Файл изображения (формат: JPEG, PNG и т.д.)
- `classifier_type`: Тип классификатора для обнаружения лиц. Варианты:
  - `eye`
  - `eyeglasses`
  - `catface`
  - `catface_extended`
  - `frontalface_alt`
  - `frontalface_alt2`
  - `frontalface_alt_tree`
  - `frontalface_default`
  - `fullbody`
  - `lefteye`
  - `license_plate`
  - `lowerbody`
  - `profileface`
  - `righteye`
  - `russian_plate`
  - `smile`
  - `upperbody`

**Ответ:**

Возвращает JSON с координатами обнаруженных лиц:

```json
{
  "faces": [
    [x, y, w, h],  // координаты первого лица
    [x, y, w, h]   // координаты второго лица
  ]
}

## Installation

To install the required dependencies, create a `requirements.txt` file with the following contents:


## Project Structure
fastapi_example/
│
├── app/
│   ├── main.py              # Точка входа в приложение
│   ├── services.py          # Логика бизнес-слоя
│   ├── controllers.py       # Контроллеры для обработки запросов
│   └── image_processing.py  # Логика обработки изображений
├── requirements.txt         # Зависимости проекта
└── Dockerfile               # Файл для сборки Docker-образа

## Installation

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) - to build and run the Docker container
- [Python 3.9](https://www.python.org/downloads/) - for local development

### Build Docker Image

To build the Docker image, run:
bash: docker build -t fastapi-example .


Run Docker Container
To run the Docker container in detached mode, use:
bash: docker run -d --name fastapi-container -p 8000:8000 fastapi-example

Local Development
To run the application locally (without Docker), use:
bash: python -m uvicorn app.main:app --reload


Dependencies
The project depends on the following packages:

fastapi
uvicorn
pytesseract
opencv-python
pillow
python-multipart
These dependencies are listed in requirements.txt.
