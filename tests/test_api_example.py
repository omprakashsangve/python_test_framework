from core.base_api import BaseAPI

def test_get_users():
    api = BaseAPI()
    response = api.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)