# app/entities/recognized_text.py

from pydantic import BaseModel

class RecognizedText(BaseModel):
    recognized_text: str

    async def getText(self):
        return self.text