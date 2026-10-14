from app import greet


def test_greet():
    assert greet("Python") == "Hello, Python!"


def test_greet_empty_name():
    assert greet("") == "Hello, !"