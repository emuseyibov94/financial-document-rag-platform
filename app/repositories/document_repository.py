import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.domain.document_status import DocumentStatus
from app.models.document import Document


class DocumentRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create_document(
        self,
        *,
        filename: str,
        content_type: str | None = None,
        file_size_bytes: int | None = None,
        checksum_sha256: str | None = None,
        storage_bucket: str | None = None,
        storage_key: str | None = None,
        status: DocumentStatus = DocumentStatus.CREATED,
    ) -> Document:
        document = Document(
            filename=filename,
            content_type=content_type,
            file_size_bytes=file_size_bytes,
            checksum_sha256=checksum_sha256,
            storage_bucket=storage_bucket,
            storage_key=storage_key,
            status=status.value,
        )

        self.session.add(document)
        self.session.commit()
        self.session.refresh(document)

        return document

    def get_document_by_id(self, document_id: uuid.UUID) -> Document | None:
        statement = select(Document).where(Document.id == document_id)
        return self.session.scalar(statement)

    def list_documents(self, limit: int = 50, offset: int = 0) -> list[Document]:
        statement = (
            select(Document)
            .order_by(Document.created_at.desc())
            .limit(limit)
            .offset(offset)
        )
        return list(self.session.scalars(statement).all())