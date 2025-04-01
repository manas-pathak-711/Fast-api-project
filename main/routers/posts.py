from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from .. import database,models,schemas,oauth
from typing import List,Optional


router = APIRouter(tags=['posts'])



@router.get("/posts",response_model=List[schemas.PostResponse])
def get_posts(db: Session = Depends(database.get_db), current_user: int = Depends(oauth.get_current_user), limit: int = 10,skip: int = 0,search: Optional[str] = ''):
    all_posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    if not all_posts :
        raise HTTPException(status_code=404,detail="There are no Posts")
    
    return all_posts



@router.post("/posts",response_model=schemas.PostResponse)
def create_post(post : schemas.PostBase, db: Session = Depends(database.get_db), current_user: int = Depends(oauth.get_current_user)):
    new_post = models.Post(title = post.title, content = post.content, published = post.published,owner_id = current_user)

    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post



@router.get("/posts/{id}",response_model=schemas.PostResponse)
def get_user_by_id(id:int, db: Session = Depends(database.get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post :
        raise HTTPException(status_code=404, detail="Post not Found!!")
    return post



@router.delete("/posts/{id}")
def delete_post(id:int, db: Session = Depends(database.get_db), current_user: int = Depends(oauth.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    if post.owner_id != current_user:
        raise HTTPException(status_code=403, detail="You don't have permission to delete this post")
    
    db.delete(post)
    db.commit()
    return {"Post":"Deleted Successfully!!"}



@router.put("/posts/{id}", response_model=schemas.PostResponse)
def update_post(post: schemas.PostBase, id: int, db: Session = Depends(database.get_db), current_user: int = Depends(oauth.get_current_user)):
    existing_post = db.query(models.Post).filter(models.Post.id == id).first()

    if not existing_post:
        raise HTTPException(status_code=404, detail="Post not found")

    if existing_post.owner_id != current_user:
        raise HTTPException(status_code=403, detail="You don't have permission to update this post")

    # Updating fields manually
    existing_post.title = post.title
    existing_post.content = post.content
    existing_post.published = post.published

    db.commit()
    db.refresh(existing_post)
    return existing_post


