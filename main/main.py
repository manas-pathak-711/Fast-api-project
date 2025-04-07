# main/main.py (correct imports)
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from main.routers import users, posts, auth, votes  # Absolute import
from main.database import engine, SessionLocal, Base  # Import actual names
from main.config import settings

# Initialize tables (if needed)
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)

@app.get("/")
def root():
    return {"message": "API is working!"}