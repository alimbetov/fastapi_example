# app/services.py

class TestService:
    @staticmethod
    def get_greeting(name: str) -> str:
        return f"Hello, {name}!"
