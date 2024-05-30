import pytest
from src.api.api_handler import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_chat_endpoint(client):
    response = client.post('/api/chat', json={"prompt": "Hello, how are you?"})
    assert response.status_code == 200
    data = response.get_json()
    assert 'response' in data
    assert isinstance(data['response'], str)
