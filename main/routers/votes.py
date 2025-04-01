from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..oauth import get_current_user
from .. import models
from .. import schemas

router = APIRouter(tags=['votes'])

@router.post("/votes/like/{id}")
def like_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    # Check if post exists
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found!")

    # Check if the user has already liked the post
    existing_like = db.query(models.Vote).filter_by(user_id=current_user, post_id=id).first()
    if existing_like:
        raise HTTPException(status_code=400, detail="You have already liked this post!")

    # Create a new like
    liked_post = models.Vote(user_id=current_user, post_id=id)
    db.add(liked_post)
    db.commit()
    db.refresh(liked_post)
    return liked_post

@router.post("/votes/removelike/{id}")
def remove_like(id: int, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    like = db.query(models.Vote).filter_by(user_id=current_user, post_id=id).first()
    if not like:
        raise HTTPException(status_code=404, detail="Like not found!")

    db.delete(like)
    db.commit()
    return {"message": "Like removed successfully"}

@router.get("/votes/{id}")
def get_number_of_likes(id: int, db: Session = Depends(get_db)):
    count = db.query(models.Vote).filter(models.Vote.post_id == id).count()
    return {"Total likes": count}
