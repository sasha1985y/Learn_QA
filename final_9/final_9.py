"""%%writefile test_store.py
import requests

# Тестовые данные
test_data = [
    {"id": 1, "petId": 101, "quantity": 2, "shipDate": "2023-10-01T00:00:00.000Z", "status": "placed", "complete": True},
    {"id": 2, "petId": 102, "quantity": 1, "shipDate": "2023-10-02T00:00:00.000Z", "status": "approved", "complete": False},
    {"id": 3, "petId": 103, "quantity": 3, "shipDate": "2023-10-03T00:00:00.000Z", "status": "delivered", "complete": True},
]

# Тест для размещения нового заказа
def test_place_order():
    url = "https://petstore.swagger.io/v2/store/order"
    for order in test_data:
        response = requests.post(url, json=order)
        assert response.status_code == 200
        assert response.json()['id'] == order['id']

# Тест для получения заказа по ID
def test_get_order_by_id():
    for order in test_data:
        url = f"https://petstore.swagger.io/v2/store/order/{order['id']}"
        response = requests.get(url)
        assert response.status_code == 200
        assert response.json()['id'] == order['id']

# Тест для удаления заказа
def test_delete_order():
    for order in test_data:
        url = f"https://petstore.swagger.io/v2/store/order/{order['id']}"
        response = requests.delete(url)
        assert response.status_code == 200

# Негативные тесты
def test_negative_cases():
    # Несуществующий ID
    url = "https://petstore.swagger.io/v2/store/order/999999"
    response = requests.get(url)
    assert response.status_code == 404

    # Некорректный формат данных
    invalid_order = {"id": "invalid", "petId": 101, "quantity": 2, "shipDate": "2023-10-01T00:00:00.000Z", "status": "placed", "complete": True}
    url = "https://petstore.swagger.io/v2/store/order"
    response = requests.post(url, json=invalid_order)
    assert response.status_code == 400

!pytest -v"""

