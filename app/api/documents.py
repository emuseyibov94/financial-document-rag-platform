import uuid

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.db.session import get_db_session
from app.repositories.document_repository import DocumentRepository
from app.schemas.document import (
    DocumentCreateRequest,
    DocumentListResponse,
    DocumentResponse,
)

router = APIRouter(prefix="/documents", tags=["documents"])


@router.post(
    "",
    response_model=DocumentResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_document(
    payload: DocumentCreateRequest,
    db: Session = Depends(get_db_session),
) -> DocumentResponse:
    repository = DocumentRepository(db)

    document = repository.create_document(
        filename=payload.filename,
        content_type=payload.content_type,
        file_size_bytes=payload.file_size_bytes,
        checksum_sha256=payload.checksum_sha256,
        storage_bucket=payload.storage_bucket,
        storage_key=payload.storage_key,
    )

    return DocumentResponse.model_validate(document)


@router.get("", response_model=DocumentListResponse)
def list_documents(
    limit: int = Query(default=50, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    db: Session = Depends(get_db_session),
) -> DocumentListResponse:
    repository = DocumentRepository(db)
    documents = repository.list_documents(limit=limit, offset=offset)

    return DocumentListResponse(
        items=[DocumentResponse.model_validate(document) for document in documents],
        count=len(documents),
    )


@router.get("/{document_id}", response_model=DocumentResponse)
def get_document(
    document_id: uuid.UUID,
    db: Session = Depends(get_db_session),
) -> DocumentResponse:
    repository = DocumentRepository(db)
    document = repository.get_document_by_id(document_id)

    if document is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found",
        )

    return DocumentResponse.model_validate(document)