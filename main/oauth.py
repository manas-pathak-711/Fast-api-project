from datetime import datetime, timedelta, timezone
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from fastapi import Depends
from sqlalchemy.orm import Session
from . import database
from .config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
TOKEN_EXPIRATION_TIME = settings.ACCESS_TOKEN_EXPIRE_MINUTES

def create_user_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=TOKEN_EXPIRATION_TIME)
    to_encode.update({"exp" : expire})

    encoded_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_token    

def verify_user(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("user_id")

        if not user_id:
            raise HTTPException(status_code=401, detail="User ID missing in token")  

        return user_id  # Return user ID if valid
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")  # Token is invalid or expired

def get_current_user(db: Session = Depends(database.get_db),token: str = Depends(oauth2_scheme)):
    id = verify_user(token=token)
    return id
