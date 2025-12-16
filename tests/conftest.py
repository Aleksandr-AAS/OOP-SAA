import pytest
from src.product import Product


@pytest.fixture
def sample_products():
    """Фикстура с тестовыми товарами"""
    return [
        Product("iPhone", "Смартфон", 79990.0, 10),
        Product("Samsung", "Смартфон", 59990.0, 15)
    ]
