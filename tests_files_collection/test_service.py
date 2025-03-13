import pytest , requests

import source.service as service

import unittest.mock as mock

##mocking data using unittest mock

@mock.patch("source.service.get_user_from_db")
def test_get_user_from_db(mocked_method):
    mocked_method.return_value = "Random Data" ## setting the mock data from the method
    user_name = service.get_user_from_db(0)

    assert user_name == "Random Data"

@mock.patch("requests.get")
def test_get_users(mock_get):
    ##mocking api response
    mock_response = mock.Mock()

    mock_response.status_code=200
    mock_response.json.return_value = {"id": 1,"name": "Nitesh kumar"}

    mock_get.return_value = mock_response

    data = service.get_users()

    assert data == {"id": 1,"name": "Nitesh kumar"}


def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        service.get_users()



@mock.patch("requests.get")
def test_get_users_error(mock_get):
    ##mocking api response
    mock_response = mock.Mock()
    mock_response.status_code = 400

    mock_get.return_value = mock_response
    ##assert error
    with pytest.raises(requests.HTTPError) as excinfo:
        service.get_users()
    assert excinfo.type is requests.HTTPError


# excinfo is an ExceptionInfo instance, which is a wrapper around the actual exception raised.
# The main attributes of interest are .type, .value and .traceback.


