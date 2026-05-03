# AI Backend Foundation

Production-ready backend foundation for AI applications built with FastAPI, PostgreSQL + pgvector, Redis, Docker Compose, SQLAlchemy, and Alembic.

## Project Status

Project 1: Production-Ready AI/ML Backend Foundation

Current capabilities:

- FastAPI backend with clean layered architecture
- Environment-based configuration
- Structured logging baseline
- Dockerized local development environment
- PostgreSQL with pgvector
- Redis dependency
- Dependency-aware health endpoint
- Docker healthchecks
- SQLAlchemy models
- Alembic migrations
- Production-like Docker Compose runtime

## Architecture

```text
Client / Browser / API Tool
        |
        v
FastAPI API
        |
        |-- Health Service
        |
        |-- PostgreSQL + pgvector
        |
        |-- Redis
```

## Runtime Modes

### Local Development Mode

Uses live code mounting and auto-reload.

```bash
make compose-up
```

API:

```text
http://127.0.0.1:8000
```

Health:

```text
http://127.0.0.1:8000/health
```

### Production-like Mode

Uses immutable container behavior with no live volume mount and no reload.

```bash
make prod-like-up
```

Apply migrations:

```bash
make prod-like-migrate
```

API:

```text
http://127.0.0.1:8001
```

Health:

```text
http://127.0.0.1:8001/health
```

## Health Endpoint

```json
{
  "status": "ok",
  "service": "ai-backend-foundation",
  "version": "0.1.0",
  "environment": "local",
  "dependencies": {
    "database": "ok",
    "redis": "ok"
  }
}
```

## Tech Stack

- Python 3.11
- FastAPI
- Pydantic / pydantic-settings
- SQLAlchemy
- Alembic
- PostgreSQL
- pgvector
- Redis
- Docker Compose
- Pytest

## Configuration

Create `.env` from `.env.example`:

```bash
cp .env.example .env
```

## Database Migrations

Create a migration:

```bash
make migration msg="your migration message"
```

Apply migrations:

```bash
make migrate
```

Apply migrations in production-like mode:

```bash
make prod-like-migrate
```

## Useful Commands

```bash
make compose-up       # start local development stack
make compose-down     # stop local development stack
make test-docker      # run tests inside Docker
make db-psql          # open PostgreSQL shell
make redis-ping       # ping Redis
make prod-like-up     # start production-like stack
make prod-like-down   # stop production-like stack
make prod-like-ps     # inspect production-like containers
```

## Current Database Tables

- `documents`
- `document_chunks`
- `alembic_version`

## Next Project

Project 2 will build the first AI feature layer:

Financial Document RAG Assistant v1

Planned capabilities:

- PDF upload
- text extraction
- chunking
- embedding generation
- pgvector semantic search
- source-grounded RAG answers
