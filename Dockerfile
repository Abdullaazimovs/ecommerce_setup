FROM python:3.11-slim

# Устанавливаем системные зависимости включая netcat
RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости и устанавливаем
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем проект
COPY . .

ENV PYTHONPATH=/app

# По умолчанию запускается сервер gunicorn (переопределяется в compose)
CMD ["gunicorn", "src.wsgi:application", "--bind", "0.0.0.0:8000"]