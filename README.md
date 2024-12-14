# Реализация REST-API информационной системы издательства.
#### Выполнил: Кузнецов Максим Дмитриевич, РИМ-140950 в рамках работы над предметом "Разработка приложений"

Необходимые переменные окружения:
- DB_URL=postgresql://{username}:{password}@localhost:5432/{db_name}
- DOCS_URL=http://127.0.0.1:8000/docs

### Структура

`publishing_app/routers` - эндпоинты

`app.py` - главная точка входа приложения

`database.py` - создание SQLModel engine, метод для дальнейшей DI сессии БД, метод запуска создания БД и таблиц

`models.py` - модели данных

`openapi_schema.json` - OpenAPI схема в виде отдельного файла

`schemas.py` - pydantic модели данных

`postgre_db.sql` - pg_dump PostgreSQL БД 
