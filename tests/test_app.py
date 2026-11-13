from main import app


def test_index_route():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"OK"


def test_health_route():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_crash_route():
    client = app.test_client()

    response = client.get("/crash")

    assert response.status_code == 500
    assert response.get_json() == {
        "status": "error",
        "message": "Intentional test error",
    }
