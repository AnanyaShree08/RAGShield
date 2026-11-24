from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_item_found():
    response = client.get("/api/v1/items/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "apple"}


def test_get_item_not_found():
    response = client.get("/api/v1/items/99")
    assert response.status_code == 404


def test_get_item_invalid_id():
    response = client.get("/api/v1/items/abc")
    assert response.status_code == 422