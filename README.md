# Реализация REST-API информационной системы издательства.
#### Выполнил: Кузнецов Максим Дмитриевич, РИМ-140950 в рамках работы над предметом "Разработка приложений"

Необходимые переменные окружения:
- DB_URL=postgresql://{username}:{password}@localhost:5432/{db_name} - строка подключения базы данных
- DOCS_URL=http://127.0.0.1:8000/docs - Swagger URL

### Структура

`publishing_app/routers` - эндпоинты

`publishing_app/app.py` - главная точка входа приложения

`publishing_app/database.py` - создание SQLModel engine, метод для дальнейшей DI сессии БД, метод запуска создания БД и таблиц

`publishing_app/models.py` - модели данных SQLModel

`publishing_app/schemas.py` - модели данных для сериализации и обработки запросами

`openapi_schema.json` - OpenAPI схема в виде отдельного файла
