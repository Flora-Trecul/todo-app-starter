"""FastAPI application entry point."""

from datetime import datetime, timezone

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from database import Base, engine, get_db

# Create all tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="To-Do API",
    description="REST API for managing to-do tasks",
    version="0.1.0",
)


@app.get("/todos", response_model=list[schemas.TodoResponse])
def list_todos(db: Session = Depends(get_db)):
    """List all todos."""
    return crud.get_todos(db)


@app.get("/reminders", response_model=list[schemas.TodoResponse])
def list_upcoming_reminders(db: Session = Depends(get_db)):
    """List todos with upcoming reminders (reminder_date in the future)."""
    now = datetime.now(timezone.utc)
    return crud.get_todos_with_upcoming_reminders(db, now)


# Subtask endpoints
@app.get("/todos/{todo_id}/subtasks", response_model=list[schemas.SubtaskResponse])
def list_subtasks(todo_id: int, db: Session = Depends(get_db)):
    """List all subtasks for a specific todo."""
    if not crud.get_todo(db, todo_id):
        raise HTTPException(status_code=404, detail="Todo not found")
    return crud.get_subtasks(db, todo_id)


@app.post("/todos/{todo_id}/subtasks", response_model=schemas.SubtaskResponse, status_code=201)
def create_subtask(todo_id: int, subtask: schemas.SubtaskCreate, db: Session = Depends(get_db)):
    """Create a new subtask for a specific todo."""
    if not crud.get_todo(db, todo_id):
        raise HTTPException(status_code=404, detail="Todo not found")
    return crud.create_subtask(db, todo_id, subtask)


@app.put("/todos/{todo_id}/subtasks/{subtask_id}", response_model=schemas.SubtaskResponse)
def update_subtask(todo_id: int, subtask_id: int, subtask: schemas.SubtaskUpdate, db: Session = Depends(get_db)):
    """Update an existing subtask."""
    if not crud.get_todo(db, todo_id):
        raise HTTPException(status_code=404, detail="Todo not found")
    updated = crud.update_subtask(db, subtask_id, subtask)
    if not updated:
        raise HTTPException(status_code=404, detail="Subtask not found")
    return updated


@app.delete("/todos/{todo_id}/subtasks/{subtask_id}", status_code=204)
def delete_subtask(todo_id: int, subtask_id: int, db: Session = Depends(get_db)):
    """Delete a subtask."""
    if not crud.get_todo(db, todo_id):
        raise HTTPException(status_code=404, detail="Todo not found")
    if not crud.delete_subtask(db, subtask_id):
        raise HTTPException(status_code=404, detail="Subtask not found")


@app.get("/todos/{todo_id}", response_model=schemas.TodoResponse)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    """Get a single todo by ID."""
    todo = crud.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@app.post("/todos", response_model=schemas.TodoResponse, status_code=201)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    """Create a new todo."""
    return crud.create_todo(db, todo)


@app.put("/todos/{todo_id}", response_model=schemas.TodoResponse)
def update_todo(todo_id: int, todo: schemas.TodoUpdate, db: Session = Depends(get_db)):
    """Update an existing todo."""
    updated = crud.update_todo(db, todo_id, todo)
    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated


@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    """Delete a todo."""
    if not crud.delete_todo(db, todo_id):
        raise HTTPException(status_code=404, detail="Todo not found")
