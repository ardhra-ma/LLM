from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_validate_intent():
    response = client.post("/validate_intent", json={"client_id": "client_a", "query": "What time is it?"})
    assert response.status_code == 200
    assert response.json() == {"query": "What time is it?", "intent": "Information Request"}

def test_configure_client():
    response = client.post("/configure-client", json={"client_name": "client_c", "intents": ["Test Intent"]})
    assert response.status_code == 200
    assert response.json() == {"message": "Client configured successfully"}

def test_get_intents():
    response = client.get("/get-intents", params={"client": "client_a"})
    assert response.status_code == 200
    assert response.json() == {
        "client": "client_a",
        "intents": [
            "Information Request", "Action Request", "Greeting", "Goodbye", 
            "Clarification", "Confirmation", "Small Talk"
        ]
    }
