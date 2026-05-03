from botocore.exceptions import BotoCoreError, ClientError

from app.storage.client import s3_client


def check_object_storage_health() -> bool:
    try:
        s3_client.list_buckets()
        return True
    except (BotoCoreError, ClientError):
        return False