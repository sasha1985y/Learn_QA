import requests
from faker import Faker
import pytest

class BaseTest:
    BASE_URL = "https://petstore.swagger.io/v2"
    
    def make_request(self, method, endpoint, headers=None, params=None, data=None):
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.request(method, url, headers=headers, params=params, json=data)
        return response


class UserDataGenerator:
    def __init__(self):
        self.faker = Faker()
    
    def generate_user_data(self):
        return {
            "id": self.faker.random_int(),
            "username": self.faker.user_name(),
            "firstName": self.faker.first_name(),
            "lastName": self.faker.last_name(),
            "email": self.faker.email(),
            "password": self.faker.password(),
            "phone": self.faker.phone_number(),
            "userStatus": 0
        }


class TestCreateUser(BaseTest):
    def test_create_user(self):
        user_data = UserDataGenerator().generate_user_data()
        response = self.make_request("POST", "/user", data=user_data)
        assert response.status_code == 200
        assert response.json()["message"] == str(user_data["id"])


class TestLoginLogout(BaseTest):
    def test_login_user(self):
        username = "testuser"
        password = "testpassword"
        response = self.make_request("GET", f"/user/login?username={username}&password={password}")
        assert response.status_code == 200
        assert "logged in" in response.json()["message"]
    
    def test_logout_user(self):
        response = self.make_request("GET", "/user/logout")
        assert response.status_code == 200
        assert "ok" in response.json()["message"]


class TestUpdateUser(BaseTest):
    def test_update_user(self):
        username = "testuser"
        updated_data = {"firstName": "UpdatedFirstName"}
        response = self.make_request("PUT", f"/user/{username}", data=updated_data)
        assert response.status_code == 200


class TestDeleteUser(BaseTest):
    def test_delete_user(self):
        # Создаем пользователя перед удалением
        user_data = UserDataGenerator().generate_user_data()
        username = user_data["username"]
        create_response = self.make_request("POST", "/user", data=user_data)
        assert create_response.status_code == 200
        
        # Теперь удаляем пользователя
        response = self.make_request("DELETE", f"/user/{username}")
        assert response.status_code == 200
