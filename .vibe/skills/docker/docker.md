---
name: docker
description: Docker and Docker Compose management for the project. Uses docker compose commands and existing configuration.
user-invocable: true
---

# Docker Guidelines

## Tech Stack
- Docker Compose

## Configuration
- Main file: `docker-compose.yml` at project root
- Services: db (PostgreSQL), api (FastAPI), web (SvelteKit frontend)

## Commands
- Build and start: `docker compose up --build`
- Start in background: `docker compose up --build -d`
- Stop: `docker compose down`
- Stop with volumes: `docker compose down -v`
- View logs: `docker compose logs -f`

## Notes
- Always use `docker compose` (not `docker-compose`)
- Database service uses PostgreSQL by default
