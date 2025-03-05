import pytest

# def setup_function(function):
#     print(f"set up function code running for{function}")
#
# def teardown_function(function):
#     print(f"tear down function code running for{function}")

@pytest.fixture
def numbers():
    a=2
    b=3
    c=8
    return [a,b,c]

def test_method1(numbers):
    x=2
    assert numbers[0]==x

@pytest.mark.skip
def test_method2(numbers):
    y=5
    assert numbers[1]==y

@pytest.mark.xfail
def test_method3(numbers):
    z=7
    assert numbers[2]==z