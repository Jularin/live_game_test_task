from fastapi.testclient import TestClient

from app.main import app
from app.utils import Field


def test_field():
    field = Field()
    assert len(field.field) == 50
    assert len(field.field[0]) == 50
    field.step()
    assert len(field.field) == 50
    assert len(field.field[0]) == 50


def test_crete_field():
    client = TestClient(app)
    response = client.post("/create_field")
    assert response.status_code == 200
    assert "id" in response.json().keys()
    assert "field" in response.json().keys()


def test_step_field_successful():
    client = TestClient(app)

    response = client.post("/create_field")
    response = client.get(f"/step/{response.json()['id']}")

    assert response.status_code == 200
    assert "id" in response.json().keys()
    assert "field" in response.json().keys()


def test_step_field_failed():
    client = TestClient(app)

    response = client.get(f"/step/123")
    assert response.status_code == 404

