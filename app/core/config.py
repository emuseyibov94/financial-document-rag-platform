from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "financial-document-rag-platform"
    app_version: str = "0.2.0"
    app_env: str = "local"
    log_level: str = "INFO"
    
    postgres_user: str = "ai_backend_user"
    postgres_password: str = "ai_backend_password"
    postgres_db: str = "ai_backend_foundation"
    postgres_host: str = "postgres"
    postgres_port: int = 5432
    database_url: str = (
        "postgresql+psycopg://ai_backend_user:ai_backend_password@postgres:5432/ai_backend_foundation"
    )

    redis_host: str = "redis"
    redis_port: int = 6379
    redis_db: int = 0
    redis_url: str = "redis://redis:6379/0"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()