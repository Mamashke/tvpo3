# Базовый образ с Python
FROM python:3.11-slim

# Рабочая директория внутри контейнера
WORKDIR /app

# Скопировать зависимости
COPY requirements.txt .

# Установить зависимости (если файл пустой — команда просто ничего не поставит)
RUN pip install --no-cache-dir -r requirements.txt

# Скопировать исходники приложения
COPY mortgage_app.py .

# Команда по умолчанию — запуск калькулятора
CMD ["python", "mortgage_app.py"]
