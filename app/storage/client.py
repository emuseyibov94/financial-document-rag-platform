import boto3
from botocore.client import BaseClient

from app.core.config import get_settings


def create_s3_client() -> BaseClient:
    settings = get_settings()

    return boto3.client(
        "s3",
        endpoint_url=settings.object_storage_endpoint,
        aws_access_key_id=settings.object_storage_access_key,
        aws_secret_access_key=settings.object_storage_secret_key,
        region_name=settings.object_storage_region,
    )


s3_client = create_s3_client()