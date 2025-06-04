# Вказати базовий образ
FROM python:3.10-slim

# Створити робочу директорію
WORKDIR /app

# Скопіювати файли
COPY . /app

# Встановити залежності
RUN pip install --no-cache-dir -r requirements.txt

# Відкрити порт
EXPOSE 8000

# Запуск сервера
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
