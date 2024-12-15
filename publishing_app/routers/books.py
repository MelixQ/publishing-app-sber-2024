from __future__ import annotations
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from models import Book, Author
from schemas import BookCreate, BookRead, BookUpdate
from database import get_session
from typing import List
import uuid

router = APIRouter()


@router.get("/api/v1/books", response_model=List[BookRead])
def read_books(
    session: Session = Depends(get_session)
):
    books = session.exec(select(Book)).all()
    return [BookRead(
        author_name=book.author.name 
            if book.author 
            else "Undefined",
        **book.model_dump()
        ) for book in books]


@router.get("/api/v1/books/{book_system_uid}", response_model=BookRead)
def read_book(
    book_system_uid: str,
    session: Session = Depends(get_session)
):
    book = session.exec(
        select(Book)
        .where(Book.system_uid == book_system_uid)
    ).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return BookRead(
        author_name=book.author.name 
            if book.author
            else "Undefined", 
        **book.model_dump()
    )


@router.post("/api/v1/books", response_model=BookRead)
def create_book(
    book: BookCreate, 
    session: Session = Depends(get_session)
):
    author = session.exec(
        select(Author)
        .where(Author.system_uid == book.author_system_uid)
    ).first()
    if not author:
        raise HTTPException(status_code=404, detail="No author in system for this book")
    
    gen_system_uid = str(uuid.uuid4())
    new_book = Book(
        **book.model_dump(exclude={"author_system_uid"}),
        system_uid=gen_system_uid,
        author_id=author.id
    )
    session.add(new_book)
    session.commit()
    session.refresh(new_book)
    return BookRead(
        author_name=author.name,
        **new_book.model_dump()
    )


@router.patch("/api/v1/books/{book_system_uid}", 
              response_model=BookRead)
def update_book(
    book_system_uid: str, 
    book_update: BookUpdate, 
    session: Session = Depends(get_session)
):
    book = session.exec(
        select(Book)
        .where(Book.system_uid == book_system_uid)
    ).first()
    if not book:
        raise HTTPException(status_code=404, detail='Book not found')
    book_data = book_update.model_dump(exclude_unset=True)
    book.sqlmodel_update(book_data)
    session.add(book)
    session.commit()
    session.refresh(book)
    return BookRead(
        author_name=book.author.name 
            if book.author
            else "Undefined",
        **book.model_dump()
    )


@router.delete("/api/v1/books/{book_system_uid}")
def delete_book(
    book_system_uid: str,
    session: Session = Depends(get_session)
):
    book = session.exec(
        select(Book)
        .where(Book.system_uid == book_system_uid)
    ).first()
    if not book:
        raise HTTPException(status_code=404, detail='Book not found')
    session.delete(book)
    session.commit()
    return {'Delete successful': True}
