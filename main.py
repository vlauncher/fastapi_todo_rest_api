from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.db import Base, engine
from app.routes import todos
import os
from dotenv import load_dotenv

load_dotenv()

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Todo routes
app.include_router(todos.router, prefix="/todos", tags=["todos"])

PORT = int(os.getenv("PORT"))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=True) 