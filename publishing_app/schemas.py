from typing import Optional
from pydantic import BaseModel, EmailStr

class BookCreateRequest(BaseModel):
    title: str
    genre: str
    page_count: int
    store_link: str
    picture: Optional[str]

    author_id: int


class AuthorCreateRequest(BaseModel):
    name: str
    info: Optional[str]
    quotes: Optional[str]


class ApplicationCreateRequest(BaseModel):
    genre: str
    target_audience_age: int
    is_18: bool
    full_name: str
    email: EmailStr
    phone: str
    social_networks: Optional[str]
    submit_file_link: str