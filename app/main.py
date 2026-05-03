import logging

from fastapi import FastAPI

import app
from app.api.routes import router
from app.core.config import get_settings
from app.core.logging import configure_logging

from app.api.documents import router as documents_router
from app.api.routes import router as health_router

from app.storage.buckets import ensure_document_bucket_exists

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    ensure_document_bucket_exists()
    logger.info("Object storage bucket ensured")

    yield

    logger.info("Application shutdown")

def create_app() -> FastAPI:
    configure_logging()
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        description="Production-style financial document RAG platform.",
        version=settings.app_version,
        lifespan=lifespan,
    )

    app.include_router(router)
    app.include_router(health_router)
    app.include_router(documents_router)

    logger.info(
        "Application started",
        extra={
            "app_name": settings.app_name,
            "app_env": settings.app_env,
            "app_version": settings.app_version,
        },
    )

    return app


app = create_app()