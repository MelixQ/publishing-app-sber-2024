from fastapi import APIRouter, HTTPException, Depends
from schemas import ApplicationCreate
from models import Application
from database import get_session
from sqlmodel import Session, select

router = APIRouter()


@router.post("/api/v1/application")
def submit_application(
    application: ApplicationCreate, 
    session: Session = Depends(get_session)
):
    existing = session.exec(
        select(Application).where(
            Application.email == application.email
        )
    ).first()
    
    if existing:
        raise HTTPException(
            status_code=400, 
            detail="Application by that e-mail was already submitted"
        )

    new_application = Application(
        **application.model_dump()
    )
    session.add(new_application)
    session.commit()
    session.refresh(new_application)
    return {'Application submitted': True}
