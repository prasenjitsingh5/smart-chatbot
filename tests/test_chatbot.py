import pytest
from src.chatbot import generate_response

def test_generate_response():
    response = generate_response("Hello, how are you?")
    assert response is not None
    assert isinstance(response, str)
    assert len(response) > 0
