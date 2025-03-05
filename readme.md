## run single test

pytest .\multiple_tests.py

## multiple tests flags : -v(tests info),-rA(output and failed tests),-k(particular test)
pytest .\multiple_tests.py -k method1 -v
pytest .\multiple_tests.py -k method2 -v

## pytest.mark.skip-----pytest.mark.xfail
pytest .\multiple_tests.py -m one
pytest .\multiple_tests.py -m two
pytest .\multiple_tests.py -m "one or two"
## grouping inside a class

## fixture--conftest.py--to globalise

## parametrize---multiple values without loop

## setup and teardown
pytest .\test_circle.py -s


## Mocking