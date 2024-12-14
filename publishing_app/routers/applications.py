from __future__ import annotations
from fastapi import APIRouter, HTTPException, Depends
from schemas import ApplicationCreateRequest
from database import get_session
from sqlmodel import Session, select

router = APIRouter()


@router.post("/api/v1/application")
def submit_application(
    request: ApplicationCreateRequest, 
    session: Session = Depends(get_session)
):
    existing = session.exec(
        select(Application).where(
            Application.email == request.email
        )
    ).first()
    
    if existing:
        raise HTTPException(
            status_code=400, 
            detail="Application by that e-mail was already submitted"
        )

    new_application = Application(
        genre=request.genre,
        target_audience_age=request.target_audience_age,
        is_18=request.is_18,
        full_name=request.full_name,
        email=request.email,
        phone=request.phone,
        socials=request.social_networks,
        submit_file_link=request.submit_file_link
    )
    session.add(new_application)
    session.commit()
    session.refresh(new_application)
    return new_application


from models import Application
Application.model_rebuild()
