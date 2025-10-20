
from fastapi import FastAPI
from .models.base import create_db_and_tables

app = FastAPI(title="AI Chatbot for Researchers")

@app.on_event("startup")
def on_startup():
    # This is for demonstration. In a real app, you'd use Alembic for migrations.
    # create_db_and_tables()
    pass

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Chatbot API"}

# Placeholder for future API routers
# from .api import users, chat
# app.include_router(users.router, prefix="/users", tags=["users"])
# app.include_router(chat.router, prefix="/chat", tags=["chat"])
