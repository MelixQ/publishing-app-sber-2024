import os

from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine, Session

load_dotenv()

DB_URL =os.environ.get('DB_URL', 'sqlite:///./publish_app.db')
engine = create_engine(DB_URL)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
