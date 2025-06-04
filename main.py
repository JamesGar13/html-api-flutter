from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Дозволити запити з Flutter
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # у продакшені вкажи точний домен
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeRequest(BaseModel):
    code: str

@app.post("/run-html")
async def run_html_code(request: CodeRequest):
    html_code = request.code.strip()

    if not html_code:
        return {"result": "Надішліть HTML-код"}

    return {
        "result": f"""<div style="border:1px solid #ccc;padding:10px;margin:10px;">
            <strong>Вивід HTML:</strong><br>
            {html_code}
        </div>"""
    }
