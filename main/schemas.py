from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Annotated, Optional

class User(BaseModel):
    email: EmailStr
    password: str

class User_out(BaseModel):
    id : int
    email: EmailStr
    created_at : datetime

class user_login(BaseModel):
    email : EmailStr
    password : str
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    

class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id : int
    owner : User_out

    class Config:
        from_attributes = True  # Helps FastAPI with ORM models


class Token(BaseModel):
    access_token : str
    token_type : str

class Token_data(BaseModel):
    id : Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, Field(ge=0, le=1)]