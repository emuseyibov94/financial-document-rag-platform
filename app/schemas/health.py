from pydantic import BaseModel


class DependencyHealth(BaseModel):
    database: str
    redis: str


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str
    environment: str
    dependencies: DependencyHealth