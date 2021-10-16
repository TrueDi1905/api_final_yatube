# api_final
### Описание
API к сервису https://github.com/TrueDi1905/yatube
- Авторизация по JWT токену
- Сериализация данных для всех моделей проекта (Post, Comment, Group, Follow)

Обработка GET, POST, PATCH, PUT и DELETE запросов к базе данных проекта Yatube
### Технологии
- Python 3.7
- Django 3.0.5
- Git
- Django REST framework 3.12.4

### Установка
- склонировать проект себе на компьютер
- Создать виртуальное окружение ``` python -m venv venv ```
- Установить зависимости ``` pip install -r backend/requirements.txt ```
- Провести миграции ``` python manage.py makemigrations ``` и ``` python manage.py migrate ``` 
- Запускаем django сервер ``` python manage.py runserver ```

Для доступа к API необходимо получить токен: Нужно выполнить POST-запрос localhost:8000/api/v1/token/ передав поля username и password. API вернет JWT-токен.
Передав токен можно будет обращаться к методам, например:
/api/v1/posts/ (GET, POST, PUT, PATCH, DELETE)
При отправке запроса передавайте токен в заголовке Authorization: Bearer <токен>
Слово Bearer здесь заменяет слово Token и означает, что за ним следует сам токен.

### Автор
Дмитрий

