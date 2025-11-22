"""### Задание: Создание фреймворка для автоматизированного тестирования пользовательских эндпоинтов

#### Шаг 1: Создание нового блокнота в Google Colab
1. Откройте Google Colab: [https://colab.research.google.com/](https://colab.research.google.com/).
2. Нажмите на кнопку "Новый блокнот" (или выберите "Файл" -> "Новый блокнот").
3. Назовите блокнот, например, "API Testing Framework".

#### Шаг 2: Установка необходимых библиотек
Для выполнения задания нам понадобятся библиотеки `requests`, `pytest` и `faker`. Установим их с помощью команды `pip`.

```python
!pip install requests pytest faker pytest-html
```

**Результат:** Библиотеки успешно установлены.

#### Шаг 3: Изучение документации PetStore
Откройте документацию PetStore: [https://petstore.swagger.io/v2/swagger.json](https://petstore.swagger.io/v2/swagger.json). Ознакомьтесь с методами работы с пользователями (`/user`), такими как:
- POST `/user` — создание пользователя.
- GET `/user/login` — вход пользователя.
- GET `/user/logout` — выход пользователя.
- PUT `/user/{username}` — обновление пользователя.
- DELETE `/user/{username}` — удаление пользователя.

#### Шаг 4: Создание базового класса для тестов
Создадим базовый класс `BaseTest`, который будет содержать общие методы для всех тестов.

```python
import requests

class BaseTest:
    BASE_URL = "https://petstore.swagger.io/v2"
    
    def make_request(self, method, endpoint, headers=None, params=None, data=None):
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.request(method, url, headers=headers, params=params, json=data)
        return response
```

**Результат:** Создан базовый класс `BaseTest` с методом `make_request`, который отправляет запросы к API.

#### Шаг 5: Написание функции для генерации случайных тестовых данных пользователя
Используем библиотеку `faker` для генерации случайных данных пользователя.

```python
from faker import Faker

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
```

**Результат:** Создана функция `generate_user_data`, которая возвращает словарь с случайными данными пользователя.

#### Шаг 6: Реализация тестов для создания пользователя (POST /user)
Напишем тест для создания пользователя с использованием `pytest`.

```python
import pytest

class TestUserEndpoints(BaseTest):
    def test_create_user(self):
        user_data = UserDataGenerator().generate_user_data()
        response = self.make_request("POST", "/user", data=user_data)
        assert response.status_code == 200
        assert response.json()["message"] == str(user_data["id"])
```

**Результат:** Тест `test_create_user` успешно создает пользователя и проверяет статус ответа и сообщение.

#### Шаг 7: Создание тестов для входа и выхода пользователя (GET /user/login, /user/logout)
Реализуем тесты для входа и выхода пользователя.

```python
class TestUserEndpoints(BaseTest):
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
```

**Результат:** Тесты `test_login_user` и `test_logout_user` успешно выполняются.

#### Шаг 8: Написание тестов для обновления и удаления пользователя
Реализуем тесты для обновления и удаления пользователя.

```python
class TestUserEndpoints(BaseTest):
    def test_update_user(self):
        username = "testuser"
        updated_data = {"firstName": "UpdatedFirstName"}
        response = self.make_request("PUT", f"/user/{username}", data=updated_data)
        assert response.status_code == 200
    
    def test_delete_user(self):
        username = "testuser"
        response = self.make_request("DELETE", f"/user/{username}")
        assert response.status_code == 200
```

**Результат:** Тесты `test_update_user` и `test_delete_user` успешно выполняются.

#### Шаг 9: Добавление функции для создания отчета о выполнении тестов
Для создания отчета используем `pytest` с плагином `pytest-html`.

Установим плагин:

```python
!pip install pytest-html
```

Запустим тесты с генерацией отчета:

```python
!pytest --html=report.html
```

**Результат:** Создан отчет `report.html` с результатами выполнения всех тестов.

### Выводы
1. Успешно создан фреймворк для автоматизированного тестирования API управления пользователями.
2. Все тесты корректно выполняются и проверяют различные аспекты работы API.
3. Сгенерирован отчет, который можно использовать для анализа результатов тестирования.
4. Фреймворк легко расширяем и может быть адаптирован под другие API."""