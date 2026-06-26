"""SQLAlchemy ORM models."""

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class Todo(Base):
    """Represents a to-do task in the database."""

    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(String(500), nullable=True)
    completed = Column(Boolean, default=False, nullable=False)
    reminder_date = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    subtasks = relationship("Subtask", back_populates="todo", cascade="all, delete-orphan")


class Subtask(Base):
    """Represents a subtask belonging to a todo."""

    __tablename__ = "subtasks"

    id = Column(Integer, primary_key=True, index=True)
    todo_id = Column(Integer, ForeignKey("todos.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(200), nullable=False)
    completed = Column(Boolean, default=False, nullable=False)
    position = Column(Integer, default=0, nullable=False)

    todo = relationship("Todo", back_populates="subtasks")
