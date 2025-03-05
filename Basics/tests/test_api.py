from http.client import responses

import pytest,requests,json

@pytest.fixture
def url():
    return "https://reqres.in"

def test_login(url):
    uri = url + "/api/login"
    data = {
    'email':'eve.holt@reqres.in',
    'password' :'cityslicka'
    }

    response = requests.post(uri,data=data)
    token = json.loads(response.text)
    print(token)

    assert response.status_code==200
    assert token['token']=="QpwL5tke4Pnpja7X4"
