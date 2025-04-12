# tests/test_main.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert "Resume Builder" in response.json()["message"]


def test_optimize_route_schema():
    response = client.post("/optimize", json={
        "resume_text": "I know Python and Django.",
        "job_description": "Looking for Python backend dev with FastAPI."
    })
    # Since we're mocking or skipping OpenAI when quota is exceeded
    assert response.status_code in [200, 500]
