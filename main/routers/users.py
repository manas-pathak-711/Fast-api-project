from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas, utils  # Correct relative imports
from sqlalchemy.exc import IntegrityError

router = APIRouter(tags=['users'])

@router.get("/users/{id}", response_model=schemas.User_out)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not Found!!")
    return user

@router.post("/users", response_model=schemas.User_out)  # Added response model
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)  # Store hashed password
    new_user = models.Users(**user.model_dump())
    new_user.password = hashed_password  # Assign hashed password

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email already registered")
    return new_user
