from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

# Base models
class BookBase(SQLModel):
    title: str
    genre: str
    page_count: int
    store_link: str
    picture: Optional[str] = None
    isbn: Optional[str] = None


class AuthorBase(SQLModel):
    name: str
    info: Optional[str] = None
    quote: Optional[str] = None


# Table models
class Book(BookBase, table=True):
    id: int = Field(default=None, primary_key=True)
    system_uid: str = Field(index=True, unique=True)
    author: "Author" = Relationship(back_populates="books") 
    author_id: Optional[int] = Field(
        default=None, 
        foreign_key="author.id", 
        ondelete="CASCADE"
    )


class Author(AuthorBase, table=True):
    id: int = Field(default=None, primary_key=True)
    system_uid: str = Field(index=True, unique=True)
    books: List["Book"] = Relationship(
        back_populates="author", 
        cascade_delete=True
    )


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
