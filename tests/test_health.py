from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check_returns_expected_shape() -> None:
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] in ["ok", "degraded"]
    assert data["service"] == "ai-backend-foundation"
    assert data["version"] == "0.1.0"
    assert data["environment"] == "local"

    assert "dependencies" in data
    assert "database" in data["dependencies"]
    assert "redis" in data["dependencies"]

    assert data["dependencies"]["database"] in ["ok", "unavailable"]
    assert data["dependencies"]["redis"] in ["ok", "unavailable"]