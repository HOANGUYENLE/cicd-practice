from fastapi.testclient import TestClient
from main import app

testClient = TestClient(app)

def test_basic_get():
    response = testClient.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello"}