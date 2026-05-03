from botocore.exceptions import ClientError

from app.core.config import get_settings
from app.storage.client import s3_client


def ensure_bucket_exists(bucket_name: str) -> None:
    try:
        s3_client.head_bucket(Bucket=bucket_name)
    except ClientError:
        s3_client.create_bucket(Bucket=bucket_name)


def ensure_document_bucket_exists() -> None:
    settings = get_settings()
    ensure_bucket_exists(settings.object_storage_bucket_documents)