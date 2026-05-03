from app.cache.health import check_redis_health
from app.core.config import get_settings
from app.db.health import check_database_health
from app.schemas.health import DependencyHealth, HealthResponse
from app.storage.health import check_object_storage_health

def get_health_status() -> HealthResponse:
    settings = get_settings()

    database_ok = check_database_health()
    redis_ok = check_redis_health()
    object_storage_ok = check_object_storage_health()

    overall_status = (
        "ok"
        if database_ok and redis_ok and object_storage_ok
        else "degraded"
    )

    return HealthResponse(
        status=overall_status,
        service=settings.app_name,
        version=settings.app_version,
        environment=settings.app_env,
        dependencies=DependencyHealth(
            database="ok" if database_ok else "unavailable",
            redis="ok" if redis_ok else "unavailable",
            object_storage="ok" if object_storage_ok else "unavailable",
        ),
    )