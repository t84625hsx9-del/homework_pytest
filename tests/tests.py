import pytest
from django.urls import reverse
from products.model import Product

@pytest.mark.django_db  # Разрешаем тесту работать с базой данных
def test_product_list_view(client):
    # Создаем тестовый товар
    Product.objects.create(name="Тестовый товар", price=100)
    
    # Имитируем GET-запрос к списку
    url = reverse('product_list')
    response = client.get(url)
    
    # Проверяем результаты
    assert response.status_code == 200
    assert "Тестовый товар" in response.content.decode()

@pytest.mark.django_db
def test_product_create_view(client):
    url = reverse('product_create')
    data = {
        'name': 'Новый товар',
        'price': '500.00',
        'description': 'Описание',
        'stock': 10
    }
    response = client.post(url, data)
    
    # Проверяем редирект после создания (success_url)
    assert response.status_code == 302
    assert Product.objects.filter(name='Новый товар').exists()