import pytest
from Concatenate import *

def test_concatenate():
    assert concatenate("Hello", "World") == "Hello World"
