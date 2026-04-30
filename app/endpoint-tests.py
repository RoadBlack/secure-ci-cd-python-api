from fastapi.testclient import TestClient
from .main import app 

client = TestClient(app)
 
def test_app():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status":"ok"}

    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": app.version}