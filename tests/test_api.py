from src.api.app import app
from fastapi.testclient import TestClient

client=TestClient(app)

def test_predict():
    r=client.post('/predict',json={"message":"I feel sad"})
    assert r.status_code==200
