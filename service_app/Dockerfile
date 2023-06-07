# Используем базовый образ Python
FROM python:3.9-alpine3.16

# Установка переменной окружения PYTHONUNBUFFERED для отключения буферизации вывода
ENV PYTHONUNBUFFERED 1

# Создание пользователя 'app' внутри контейнера
RUN adduser -D app
USER app

# Установка рабочей директории внутри контейнера
WORKDIR /code

# Установка зависимостей проекта
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода проекта в контейнер
COPY . /code/

# Запуск команды для создания миграций и применения их к базе данных
RUN python manage.py makemigrations
RUN python manage.py migrate

# Открытие порта для веб-приложения
EXPOSE 8000

# Команда для запуска сервера Django в контейнере
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
