from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from .routers import users,posts,auth,votes
from main import database
from .config import settings

# # Create database tables
# posts.models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)