from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Learn Pytest",
            "completed": False
        }
    )

    assert response.status_code == 201
    data = response.json()

    assert data["title"] == "Learn Pytest"
    assert data["completed"] is False
    assert "id" in data


def test_get_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Testing Task",
            "completed": False
        }
    )

    task_id = response.json()["id"]

    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["id"] == task_id


def test_get_nonexistent_task():
    response = client.get("/tasks/99999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"


def test_update_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Old Task",
            "completed": False
        }
    )

    task_id = response.json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={
            "title": "Updated Task",
            "completed": True
        }
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Updated Task"
    assert response.json()["completed"] is True


def test_delete_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Delete Me",
            "completed": False
        }
    )

    task_id = response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["message"] == "Task deleted successfully"


def test_delete_nonexistent_task():
    response = client.delete("/tasks/99999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"
def test_create_task_validation_error():
    response = client.post(
        "/tasks",
        json={
            "completed": False
        }
    )

    assert response.status_code == 422
