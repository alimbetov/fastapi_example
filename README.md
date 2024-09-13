# FastAPI Example Project

This project demonstrates a FastAPI application with Docker integration and local development setup.

- **`/upload_image/`** (POST): Uploads an image file and processes it. The image is saved to the `uploaded_images/` directory, and the text recognized from the image is returned.
  
  **Request:**
  - `file` (form-data): The image file to be uploaded.
  
  **Response:**
  - `text` (string): The text recognized from the image.

- **`/greet/{name}`** (GET): Returns a greeting message. The `name` path parameter is used to generate a personalized greeting.
  
  **Request:**
  - `name` (path parameter): The name of the person to greet.
  
  **Response:**
  - `message` (string): A personalized greeting message.

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
