from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_document_returns_created_document() -> None:
    response = client.post(
        "/documents",
        json={
            "filename": "test-contract.pdf",
            "content_type": "application/pdf",
            "file_size_bytes": 100,
            "checksum_sha256": "b" * 64,
            "storage_bucket": "documents",
            "storage_key": "raw/test-contract.pdf",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["filename"] == "test-contract.pdf"
    assert data["status"] == "created"
    assert data["checksum_sha256"] == "b" * 64
    assert "id" in data


def test_list_documents_returns_items() -> None:
    response = client.get("/documents")

    assert response.status_code == 200

    data = response.json()

    assert "items" in data
    assert "count" in data
    assert isinstance(data["items"], list)