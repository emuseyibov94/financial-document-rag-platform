import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.domain.document_status import DocumentStatus


class DocumentCreateRequest(BaseModel):
    filename: str = Field(..., min_length=1, max_length=255)
    content_type: str | None = Field(default=None, max_length=100)
    file_size_bytes: int | None = Field(default=None, ge=0)
    checksum_sha256: str | None = Field(default=None, min_length=64, max_length=64)
    storage_bucket: str | None = Field(default=None, max_length=100)
    storage_key: str | None = Field(default=None, max_length=500)


class DocumentResponse(BaseModel):
    id: uuid.UUID
    filename: str
    content_type: str | None
    file_size_bytes: int | None
    checksum_sha256: str | None
    storage_bucket: str | None
    storage_key: str | None
    status: DocumentStatus
    error_message: str | None
    created_at: datetime
    updated_at: datetime
    processed_at: datetime | None

    model_config = ConfigDict(from_attributes=True)


class DocumentListResponse(BaseModel):
    items: list[DocumentResponse]
    count: int