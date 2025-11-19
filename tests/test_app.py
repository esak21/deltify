
from src.deltify import app

def test_greet():
    print("Testing")
    assert app.greet("uv") == "Hello, uv!"