from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import subprocess
from fastapi.responses import HTMLResponse



app = FastAPI()

# Дозволяємо CORS для Flutter-додатку
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Заміни "*" на адресу твого додатку
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🟢 Головна сторінка (для перевірки)
@app.get("/")
def read_root():
    return {"message": "API для виконання HTML-коду запущено."}

# 🔵 Модель для запиту
class CodeInput(BaseModel):
    code: str

# 🔴 Ендпоінт для запуску HTML-коду
@app.post("/run-html")
def run_html_code(input: CodeInput):
    try:
        # Зберігаємо код у файл
        with open("temp.html", "w", encoding="utf-8") as f:
            f.write(input.code)

        # Запускаємо у браузері або повертаємо HTML-рядок
        return HTMLResponse(content=input.code)
    except Exception as e:
        return {"error": str(e)}
