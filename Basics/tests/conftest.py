import pytest

### set up and teardown

##m1
# @pytest.fixture(autouse=True)
# def setup():
#     print(f"set up code running for")
#
# @pytest.fixture(autouse=True)
# def teardown():
#     print(f"tear down code running for")


# ###m2
# @pytest.fixture(autouse=True)
# def setup_and_teardown():
#     print(f"set up code running")
#     yield
#     print(f"tear down code running")

##Hooks

def setup_function(function):
    print(f"set up function code running for{function}")

def teardown_function(function):
    print(f"tear down function code running for{function}")

# def setup_module(module):
#     print(f"set up module code running for{module}")
#
# def teardown_module(function):
#     print(f"tear down module code running for{function}")