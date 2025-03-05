import pytest

@pytest.mark.one
def test_method1():
    x=5
    y=10
    assert x==y

@pytest.mark.two
def test_method2():
    x=5
    y=10
    assert x+5==y