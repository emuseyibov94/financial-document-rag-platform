from redis.exceptions import RedisError

from app.cache.redis_client import redis_client


def check_redis_health() -> bool:
    try:
        return redis_client.ping()
    except RedisError:
        return False