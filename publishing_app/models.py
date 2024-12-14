from __future__ import annotations
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy.orm import Mapped, relationship

class BookBase(SQLModel):
    title: str
    genre: str
    page_count: int
    store_link: str
    picture: Optional[str] = None


class Book(BookBase, table=True):
    id: int = Field(default=None, primary_key=True)
    author: Mapped[Optional['Author']] = Relationship(sa_relationship=relationship(back_populates="books"))
    author_id: int = Field(foreign_key="author.id")


class BookUpdate(SQLModel):
    title: str | None = None
    genre: str | None = None
    page_count: int | None = None
    store_link: str | None = None
    picture: Optional[str] | None = None


class AuthorBase(SQLModel):
    name: str
    info: Optional[str] = None
    quotes: Optional[str] = None


class Author(AuthorBase, table=True):
    id: int = Field(default=None, primary_key=True)
    books: Mapped[List['Book']] = Relationship(sa_relationship=relationship(back_populates="author"))


class AuthorUpdate(SQLModel):
    name: str | None = None
    info: str | None = None
    quotes: Optional[str] | None = None


class Application(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    genre: str
    target_audience_age: int
    is_18: bool
    full_name: str
    email: str
    phone: str
    socials: Optional[str] = None
    submit_file_link: str
