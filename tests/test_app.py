from main import app


def test_root_returns_ok():
    response = app.test_client().get("/")

    assert response.status_code == 200
    assert response.get_data(as_text=True) == "OK"


def test_health_returns_ok():
    response = app.test_client().get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
