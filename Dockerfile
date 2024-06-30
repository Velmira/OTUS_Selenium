# Устанавливаю базовый образ
FROM python:3.8-alpine

# Устанавливаю рабочую директорию внутри контейнера
# Диретокрия будет создана если её не было
# Будет в дальнешйем использовать как базовая
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Выполняем необходимые команды
RUN pip install -U pip
RUN pip install -r requirements.txt

# Копируем остальные файлы проекта
COPY .. .

# Устанавливаем команду по умолчанию для запуска тестов
CMD ["pytest --browser ${browser} --alluredir=/app/allure-results"]

