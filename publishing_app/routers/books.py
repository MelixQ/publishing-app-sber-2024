from __future__ import annotations
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from schemas import BookCreateRequest
from database import get_session

router = APIRouter()


@router.get("/api/v1/books")
def list_books(session: Session = Depends(get_session)):
    books = session.exec(select(Book)).all()
    return books


@router.get("/api/v1/books/{book_id}")
def get_book(book_id: int, session: Session = Depends(get_session)):
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.post("/api/v1/books")
def create_book(
    request: BookCreateRequest, 
    session: Session = Depends(get_session)
):
    new_book = Book(
        title=request.title,
        genre=request.genre,
        page_count=request.page_count,
        store_link=request.store_link,
        picture=request.picture,
        author_id=request.author_id
    )
    session.add(new_book)
    session.commit()
    session.refresh(new_book)
    return new_book


@router.patch("/api/v1/books/{book_id}")
def patch_book(
    book_id: int, 
    book: BookUpdate, 
    session: Session = Depends(get_session)
):
    query = select(Book).where(Book.id == book_id)
    db_book = session.exec(query).first()
    if not db_book:
        raise HTTPException(status_code=404, detail='Book not found')
    book_data = book.model_dump(exclude_unset=True)
    db_book.sqlmodel_update(book_data)
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book


@router.delete("/api/v1/books/{book_id}")
def delete_book(book_id: int, session: Session = Depends(get_session)):
    query = select(Book).where(Book.id == book_id)
    book = session.exec(query).first()
    if not book:
        raise HTTPException(status_code=404, detail='Book not found')
    session.delete(book)
    session.commit()
    return {'Delete successful': True}


from models import Book, BookUpdate
Book.model_rebuild()
BookUpdate.model_rebuild()
