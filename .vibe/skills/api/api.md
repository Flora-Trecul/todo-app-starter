---
name: api
description: FastAPI backend development with SQLAlchemy and Pydantic. Follows PEP 8, type hints, and existing project patterns.
user-invocable: true
---

# API Development Guidelines

## Tech Stack
- Framework: FastAPI
- ORM: SQLAlchemy 2.0
- Validation: Pydantic v2
- Database: PostgreSQL (via `DATABASE_URL`)

## Structure
- Models: `api/models/`
- Schemas: `api/schemas/`
- CRUD: `api/crud/`
- Endpoints: `api/routers/`
- Tests: `api/tests/`

## Conventions
- snake_case for functions/variables
- Type hints mandatory
- Pydantic models for request/response validation
- SQLAlchemy models with declarative base

## Testing
- Use pytest for API tests
- TestClient for endpoint testing
- Fixtures in `api/tests/conftest.py`

## Commands
- Run tests: `cd api && uv run pytest`
- Run server: `cd api && uv run uvicorn main:app --reload`
