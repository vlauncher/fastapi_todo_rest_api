from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.config.db import SessionLocal
from app.schema.todos import TodoCreate, TodoRead
from app.services.todos import create_todo, get_todos, get_todo, update_todo, delete_todo

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TodoRead)
def create_todo_route(todo: TodoCreate, db: Session = Depends(get_db)):
    return create_todo(db, todo)

@router.get("/", response_model=List[TodoRead])
def read_todos_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_todos(db, skip, limit)

@router.get("/{todo_id}", response_model=TodoRead)
def read_todo_route(todo_id: int, db: Session = Depends(get_db)):
    todo = get_todo(db, todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.put("/{todo_id}", response_model=TodoRead)
def update_todo_route(todo_id: int, todo: TodoCreate, db: Session = Depends(get_db)):
    updated_todo = update_todo(db, todo_id, todo)
    if updated_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated_todo

@router.delete("/{todo_id}", response_model=TodoRead)
def delete_todo_route(todo_id: int, db: Session = Depends(get_db)):
    deleted_todo = delete_todo(db, todo_id)
    if deleted_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return deleted_todo
