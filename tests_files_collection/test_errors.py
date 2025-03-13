import pytest



def test_exception_in_group():
    with pytest.raises(ExceptionGroup) as excinfo:
        raise ExceptionGroup(
            "Group message",
            [
                RuntimeError("Exception 123 raised"),
            ],
        )
    assert excinfo.group_contains(RuntimeError, match=r".* 123 .*")
    assert not excinfo.group_contains(TypeError)


#By default group_contains() will recursively search for a matching exception at any level of nested ExceptionGroup instances.
# You can specify a depth keyword parameter if you only want to match an exception at a specific level; exceptions contained directly in the top ExceptionGroup would match depth=1.

def test_exception_in_group_at_given_depth():
    with pytest.raises(ExceptionGroup) as excinfo:
        raise ExceptionGroup(
            "Group message",
            [
                RuntimeError(),
                ExceptionGroup(
                    "Nested group",
                    [
                        TypeError(),
                    ],
                ),
            ],
        )
    assert excinfo.group_contains(RuntimeError, depth=1)
    assert excinfo.group_contains(TypeError, depth=2)
    assert not excinfo.group_contains(RuntimeError, depth=2)
    assert not excinfo.group_contains(TypeError, depth=1)


# fully supported
# def func(x):
#     if x <= 0:
#         raise ValueError("x needs to be larger than zero")
#
#
# pytest.raises(ValueError, func, x=-1)

# xfail mark and pytest.raises
# def f():
#     raise IndexError()
#
#
# @pytest.mark.xfail(raises=IndexError)
# def test_f():
#     f()