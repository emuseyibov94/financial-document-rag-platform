import logging

from fastapi import FastAPI

from app.api.routes import router
from app.core.config import get_settings
from app.core.logging import configure_logging

logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    configure_logging()
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        description="Production-ready backend foundation for AI applications.",
        version=settings.app_version,
    )

    app.include_router(router)

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