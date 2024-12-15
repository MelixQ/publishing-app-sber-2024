from typing import Optional, List
from models import BookBase, AuthorBase
from pydantic import BaseModel, EmailStr


# Book schemas
class BookCreate(BookBase):
    author_system_uid: str


class BookRead(BookBase):
    system_uid: str
    author_name: str


class BookUpdate(BaseModel):
    title: Optional[str] = None
    genre: Optional[str] = None
    page_count: Optional[int] = None
    store_link: Optional[str] = None
    picture: Optional[str] = None
    isbn: Optional[str] = None


# Author schemas
class AuthorCreate(AuthorBase):
    pass 


class AuthorRead(AuthorBase):
    system_uid: str
    books: List[BookRead] = []


class AuthorUpdate(AuthorBase):
    name: Optional[str] = None
    info: Optional[str] = None
    quote: Optional[str] = None


# Application schema
class ApplicationCreate(BaseModel):
    genre: str
    target_audience_age: int
    is_18: bool
    full_name: str
    email: EmailStr
    phone: str
    social_networks: Optional[str]
    submit_file_link: str
