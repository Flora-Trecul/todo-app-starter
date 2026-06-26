"""CRUD operations for the Todo and Subtask models."""

from datetime import datetime

from sqlalchemy.orm import Session

from models import Subtask, Todo
from schemas import SubtaskCreate, SubtaskUpdate, TodoCreate, TodoUpdate


def get_todos(db: Session) -> list[Todo]:
    """Return all todos ordered by creation date (newest first)."""
    return db.query(Todo).order_by(Todo.created_at.desc()).all()


def get_todo(db: Session, todo_id: int) -> Todo | None:
    """Return a single todo by ID, or None if not found."""
    return db.query(Todo).filter(Todo.id == todo_id).first()


def create_todo(db: Session, todo: TodoCreate) -> Todo:
    """Create a new todo and return it."""
    db_todo = Todo(**todo.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def update_todo(db: Session, todo_id: int, todo: TodoUpdate) -> Todo | None:
    """Update an existing todo. Returns None if not found."""
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not db_todo:
        return None
    for key, value in todo.model_dump(exclude_unset=True).items():
        setattr(db_todo, key, value)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def delete_todo(db: Session, todo_id: int) -> bool:
    """Delete a todo by ID. Returns True if deleted, False if not found."""
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not db_todo:
        return False
    db.delete(db_todo)
    db.commit()
    return True


def get_todos_with_upcoming_reminders(db: Session, now: datetime) -> list[Todo]:
    """Return todos with reminder_date in the future, ordered by reminder_date."""
    return (
        db.query(Todo)
        .filter(Todo.reminder_date.isnot(None), Todo.reminder_date > now)
        .order_by(Todo.reminder_date.asc())
        .all()
    )


# Subtask CRUD operations

def get_subtasks(db: Session, todo_id: int) -> list[Subtask]:
    """Return all subtasks for a todo, ordered by position."""
    return db.query(Subtask).filter(Subtask.todo_id == todo_id).order_by(Subtask.position.asc()).all()


def get_subtask(db: Session, subtask_id: int) -> Subtask | None:
    """Return a single subtask by ID, or None if not found."""
    return db.query(Subtask).filter(Subtask.id == subtask_id).first()


def create_subtask(db: Session, todo_id: int, subtask: SubtaskCreate) -> Subtask:
    """Create a new subtask for a todo and return it."""
    db_subtask = Subtask(**subtask.model_dump(), todo_id=todo_id)
    db.add(db_subtask)
    db.commit()
    db.refresh(db_subtask)
    return db_subtask


def update_subtask(db: Session, subtask_id: int, subtask: SubtaskUpdate) -> Subtask | None:
    """Update an existing subtask. Returns None if not found."""
    db_subtask = db.query(Subtask).filter(Subtask.id == subtask_id).first()
    if not db_subtask:
        return None
    for key, value in subtask.model_dump(exclude_unset=True).items():
        setattr(db_subtask, key, value)
    db.commit()
    db.refresh(db_subtask)
    return db_subtask


def delete_subtask(db: Session, subtask_id: int) -> bool:
    """Delete a subtask by ID. Returns True if deleted, False if not found."""
    db_subtask = db.query(Subtask).filter(Subtask.id == subtask_id).first()
    if not db_subtask:
        return False
    db.delete(db_subtask)
    db.commit()
    return True
