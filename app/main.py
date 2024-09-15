# app/main.py
from fastapi import FastAPI
from .controllers import router

app = FastAPI()

# Подключаем роутеры
app.include_router(router)

@router.get("/")
async def root():
    return {"message": "Welcome to FastAPI ImageProcess Application"}
