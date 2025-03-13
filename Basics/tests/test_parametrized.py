import pytest

# In case the values provided to parametrize result in an empty list -
# for example, if they’re dynamically generated by some function - the behaviour of pytest is defined by the empty_parameter_set_mark option.


@pytest.mark.parametrize("x,y,z",[(1,2,3),(4,5,6)])
def test_method1(x,y,z):
    assert x+y==z

@pytest.mark.parametrize("input,output",[(2,4),(5,25),pytest.param(7, 42, marks=pytest.mark.xfail)])
def test_param(input,output):
    assert input*input == output