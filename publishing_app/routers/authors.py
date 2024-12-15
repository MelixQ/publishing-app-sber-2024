from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from models import Author
from schemas import AuthorCreate, AuthorRead, AuthorUpdate, BookRead
from database import get_session
import uuid

router = APIRouter()

@router.get("/api/v1/authors", response_model=List[AuthorRead])
def read_authors(
    session: Session = Depends(get_session)
):
    authors = session.exec(select(Author)).all()
    author_list = []
    for author in authors:
        books = [BookRead(author_name=book.author.name 
                            if book.author 
                            else "Undefined", 
                        **book.model_dump()) for book in author.books]
        author_list.append(AuthorRead(books=books, 
                                      **author.model_dump()))
    return author_list


@router.get("/api/v1/authors/{author_system_uid}", response_model=AuthorRead)
def read_author(
    author_system_uid: str, 
    session: Session = Depends(get_session)
):
    author = session.exec(
        select(Author)
        .where(Author.system_uid == author_system_uid)
    ).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

    books = [BookRead(
        author_name=book.author.name 
            if book.author 
            else "Undefined", 
        **book.model_dump()) for book in author.books]
    return AuthorRead(books=books, **author.model_dump())


@router.post("/api/v1/authors", response_model=AuthorRead)
def create_author(
    author: AuthorCreate, 
    session: Session = Depends(get_session)
):
    gen_system_uid = str(uuid.uuid4())
    new_author = Author(
        **author.model_dump(),
        system_uid=gen_system_uid
    )
    session.add(new_author)
    session.commit()
    session.refresh(new_author)
    return AuthorRead(books=[], **new_author.model_dump())


@router.patch("/api/v1/authors/{author_system_uid}",
              response_model=AuthorRead)
def update_author(
    author_system_uid: str, 
    author_update: AuthorUpdate, 
    session: Session = Depends(get_session)
):
    author = session.exec(
        select(Author)
        .where(Author.system_uid == author_system_uid)
    ).first()
    if not author:
        raise HTTPException(status_code=404, detail='Author not found')
    author_data = author_update.model_dump(exclude_unset=True)
    author.sqlmodel_update(author_data)
    session.add(author)
    session.commit()
    session.refresh(author)
    books = [BookRead(
        author_name=book.author.name 
            if book.author 
            else "Undefined", 
        **book.model_dump()) for book in author.books]
    return AuthorRead(books=books, **author.model_dump())


@router.delete("/api/v1/authors/{author_system_uid}")
def delete_author(
    author_system_uid: str, 
    session: Session = Depends(get_session)
):
    author = session.exec(
        select(Author)
        .where(Author.system_uid == author_system_uid)
    ).first()
    if not author:
        raise HTTPException(status_code=404, detail='Author not found')
    
    session.delete(author)
    session.commit()
    return {'Delete successful': True}
