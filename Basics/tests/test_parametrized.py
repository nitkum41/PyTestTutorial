import pytest


@pytest.mark.parametrize("x,y,z",[(1,2,3),(4,5,6)])
def test_method1(x,y,z):
    assert x+y==z

