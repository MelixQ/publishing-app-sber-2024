from __future__ import annotations
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from schemas import AuthorCreateRequest
from database import get_session

router = APIRouter()

@router.get("/api/v1/authors")
def list_authors(session: Session = Depends(get_session)):
    authors = session.exec(select(Author)).all()
    return authors


@router.get("/api/v1/authors/{author_id}")
def get_author(author_id: int, session: Session = Depends(get_session)):
    author = session.get(Author, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@router.post("/api/v1/authors")
def create_author(
    request: AuthorCreateRequest, 
    session: Session = Depends(get_session)
):
    new_author = Author(
        name=request.name,
        info=request.info,
        quotes=request.quotes
    )
    session.add(new_author)
    session.commit()
    session.refresh(new_author)
    return new_author


@router.patch("/api/v1/authors/{author_id}")
def patch_author(
    author_id: int, 
    author: AuthorUpdate, 
    session: Session = Depends(get_session)
):
    query = select(Author).where(Author.id == author_id)
    db_author = session.exec(query).first()
    if not db_author:
        raise HTTPException(status_code=404, detail='Author not found')
    author_data = author.model_dump(exclude_unset=True)
    db_author.sqlmodel_update(author_data)
    session.add(db_author)
    session.commit()
    session.refresh(db_author)
    return db_author


@router.delete("/api/v1/authors/{author_id}")
def delete_author(author_id: int, session: Session = Depends(get_session)):
    query = select(Author).where(Author.id == author_id)
    author = session.exec(query).first()
    if not author:
        raise HTTPException(status_code=404, detail='Author not found')
    session.delete(author)
    session.commit()
    return {'Delete successful': True}


from models import Author, AuthorUpdate
Author.model_rebuild()
AuthorUpdate.model_rebuild()
