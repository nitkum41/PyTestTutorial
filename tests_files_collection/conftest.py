import pytest

import source.shapes as shapes

@pytest.fixture
def get_rectangle():
    return shapes.Rectangle(4,5) ## get object

@pytest.fixture
def get_other_rectangle():
    return shapes.Rectangle(5, 4)  ## get object

##global patch
#If you want to prevent the “requests” library from performing http requests in all your tests,

@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    """Remove requests.sessions.Session.request for all tests."""
    monkeypatch.delattr("requests.sessions.Session.request")