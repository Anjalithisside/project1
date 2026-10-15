from fastapi.testclient import TestClient

from app.main import app


def test_health_reports_database_connected():
    r = TestClient(app).get("/api/v1/health")
    assert r.status_code == 200
    assert r.json()["database"] == "connected"
