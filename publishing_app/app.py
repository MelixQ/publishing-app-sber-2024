import os

from fastapi import FastAPI
from dotenv import load_dotenv
from database import create_db_and_tables
from contextlib import asynccontextmanager
from fastapi.responses import HTMLResponse
from routers import authors, books, applications


load_dotenv()

DOCS_URL =os.environ.get('DOCS_URL','http://127.0.0.1:8000/docs')


root_page = f"""
<html>
    <body>
        <h1>
            API Docs расположен тут: <a href="{DOCS_URL}">{DOCS_URL}</a>
        </h1>
    </body>
</html>
"""


@asynccontextmanager
async def db_event_lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(
    title='API информационной системы издательства',
    description='Выполнено: Кузнецов Максим Дмитриевич, РИМ-140950',
    lifespan=db_event_lifespan)


app.include_router(authors.router, tags=["Authors"])
app.include_router(books.router, tags=["Books"])
app.include_router(applications.router, tags=["Applications"])


@app.get("/")
def root():
    """Homepage"""
    return HTMLResponse(content=root_page, status_code=200)
