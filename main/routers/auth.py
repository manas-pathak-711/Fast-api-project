from fastapi import APIRouter, Depends, HTTPException, responses
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models,utils, oauth
# from fastapi.security.oauth2 import OAuth2PasswordRequestForm


router = APIRouter(tags=['Authentication'])


@router.post("/login")
def login(user_cred :schemas.user_login ,db: Session = Depends(get_db)):

    user = db.query(models.Users).filter(models.Users.email == user_cred.email).first()

    if not user:
        raise HTTPException(status_code=403, detail="Invalid Credentials")
    
    if not utils.verify(user_cred.password, user.password):
        raise HTTPException(status_code=403, detail="Invalid Credentials")
    
    access_token = oauth.create_user_token(data = {"user_id" : user.id})
    
    return {"access_token" : access_token,
            "token_type" : "bearer"}

    

