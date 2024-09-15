# FastAPI Example Project

API Documentation
Endpoints
1.Upload and Process of Optical Character Recognition
POST /img-ocr/

Upload an image and perform OCR (Optical Character Recognition) 
to extract text.

Request Body:
file (form-data): The image file to be processed.

Responses:
200 OK: Returns a JSON object with the recognized text.
json
Копировать код
{
  "text": "Recognized text from the image."
}
500 Internal Server Error: If an error occurs during processing.


2.Get Face Embedding
POST /face_embedding/

Upload an image and get the face embedding.
Request Body:
file (form-data): The image file to be processed.
inIsDeep (query parameter, optional): Boolean to enforce deep face embedding.
inEnforceFaceDetection (query parameter, optional): Boolean to enforce face detection.
Responses:
200 OK: Returns a JSON object with the face embedding.
json
{
  "embedding": [0.1, 0.2, ..., 0.5]
}
400 Bad Request: If the uploaded file is not an image or processing fails.


3.Detect Faces
POST /detect_faces/
Upload an image and detect faces in it.
Request Body:
file (form-data): The image file to be processed.
classifier_type (query parameter, optional): Type of face classifier to use for face detection. Available options include:
eye: Detects eyes in the image.
eyeglasses: Detects eyeglasses.
catface: Detects faces of cats.
catface_extended: Detects faces of cats with extended features.
frontalface_alt: Detects frontal faces (alternative model).
frontalface_alt2: Detects frontal faces (second alternative model).
frontalface_alt_tree: Detects frontal faces using a tree-based model.
frontalface_default: Detects frontal faces (default model).
fullbody: Detects full bodies.
lefteye: Detects left eyes.
license_plate: Detects license plates.
lowerbody: Detects lower bodies.
profileface: Detects profile faces.
righteye: Detects right eyes.
russian_plate: Detects Russian license plates.
smile: Detects smiles.
upperbody: Detects upper bodies.

Responses:
200 OK: Returns a JSON object with the detected faces' coordinates.
json
{
  "faces": [[x1, y1, x2, y2], [x3, y3, x4, y4]]
}
400 Bad Request: If the uploaded file is not an image or processing fails.

File Handling
Files are saved with a SHA-256 hash to ensure unique filenames.
Uploaded files are temporarily stored in the uploaded_images/ directory and deleted after processing.


## Installation

To install the required dependencies, create a `requirements.txt` file with the following contents:
fastapi==0.95.1
uvicorn==0.23.1
deepface==0.0.75
pytesseract==0.3.10
opencv-python==4.7.0.72
pillow==9.5.0
python-multipart==0.0.6
numpy==1.25.2
tensorflow==2.15.0
keras==2.15.0
opencv-python-headless==4.7.0.72

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
