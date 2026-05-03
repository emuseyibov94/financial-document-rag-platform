from enum import StrEnum


class DocumentStatus(StrEnum):
    CREATED = "created"
    STORED = "stored"
    QUEUED = "queued"
    PROCESSING = "processing"
    INDEXED = "indexed"
    FAILED = "failed"