# Использование уязвимого образа
FROM debian:stretch

# Добавление файлов в контейнер
COPY . /app

# Установка пакетов без проверки подлинности
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    curl \
    && apt-get clean

# Запуск приложения
CMD ["python", "/app/app.py"]
