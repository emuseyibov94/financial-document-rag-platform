# Architecture

## Project 1: AI Backend Foundation

```text
Client
  |
  v
FastAPI API
  |
  |-- app/api         HTTP routes
  |-- app/services    business logic
  |-- app/schemas     request/response contracts
  |-- app/core        config and logging
  |-- app/db          database engine and health checks
  |-- app/cache       Redis client and health checks
  |-- app/models      SQLAlchemy models
  |
  |-- PostgreSQL + pgvector
  |-- Redis
```

## Request Flow

```text
GET /health
  |
  v
app/api/routes.py
  |
  v
app/services/health_service.py
  |
  |-- app/db/health.py
  |-- app/cache/health.py
  |
  v
HealthResponse
```

## Runtime Modes

### Development

- live source code mounted into container
- Uvicorn reload enabled
- fast feedback loop

### Production-like

- source code comes from Docker image
- no live mount
- no reload
- restart policy enabled
- container healthchecks enabled
```