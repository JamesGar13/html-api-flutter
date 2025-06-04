# Офіційний образ Python
FROM python:3.11

# Встановлення робочої директорії
WORKDIR /app

# Копіювання файлів
COPY . .

# Встановлення залежностей
RUN pip install --no-cache-dir -r requirements.txt

# Запуск FastAPI через Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
