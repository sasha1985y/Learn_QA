"""!pip install requests pytest

import requests

# Функция для создания нового питомца
def create_pet(pet_id, name, status="available"):
    url = "https://petstore.swagger.io/v2/pet"
    headers = {"Content-Type": "application/json"}
    payload = {
        "id": pet_id,
        "name": name,
        "status": status
    }
    response = requests.post(url, json=payload, headers=headers)
    return response

def test_get_pet_by_id():
    # Сначала создаем нового питомца
    pet_id = 1
    pet_name = "murrrzik"
    create_pet(pet_id, pet_name, status="available")

    # Получаем информацию о питомце по ID
    url = f"https://petstore.swagger.io/v2/pet/{pet_id}"
    response = requests.get(url)

    # Проверяем статус-код и содержимое ответа
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.json()["id"] == pet_id, f"Expected pet ID {pet_id}, but got {response.json()['id']}"
    assert response.json()["name"] == pet_name, f"Expected pet name {pet_name}, but got {response.json()['name']}"
    print(response.json()["id"])
    print(response.json()["name"])
    print(response.status_code)
    print(response)
print(test_get_pet_by_id())

def test_update_pet():
    # Сначала создаем нового питомца
    pet_id = 12
    pet_name = "Waska"
    status="pending"
    create_pet(pet_id, pet_name, status)

    print(f"идентефикатор при создании: {pet_id}")
    print(f"имя при создании: {pet_name}")
    print(f"статус при создании: {status} \n ________________________________")

    # Обновляем информацию о питомце
    url = "https://petstore.swagger.io/v2/pet"
    headers = {"Content-Type": "application/json"}
    updated_name = "Max"
    payload = {
        "id": 303,
        "name": updated_name,
        "status": "sold"
    }
    response = requests.put(url, json=payload, headers=headers)

    # Проверяем статус-код и обновленное содержимое
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.json()["name"] == updated_name, f"Expected updated pet name {updated_name}, but got {response.json()['name']}"
    print(f"идентефикатор после обновления: {response.json()["id"]}")
    print(f"статус после обновления: {response.json()["status"]}")
    print(f"имя после обновления: {response.json()["name"]}")
    print(response.status_code)
print(test_update_pet())

def test_delete_pet():
    # Сначала создаем нового питомца
    pet_id = 45
    pet_name = "Tuzik"
    create_pet(pet_id, pet_name)

    # Удаляем питомца по ID
    url = f"https://petstore.swagger.io/v2/pet/{pet_id}"
    response = requests.delete(url)

    # Проверяем статус-код
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    print(f"питомец id: {pet_id} по имени: {pet_name} удалён? {response.status_code}")

    # Проверяем, что питомец действительно удален
    response = requests.get(url)
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"
    print(f"питомец id: {pet_id} по имени: {pet_name} есть в базе? {response.status_code}")
test_delete_pet()"""