import pytest
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
from src.product import Product
from src.Category import Category


@pytest.fixture
def sample_products():
    """Фикстура с тестовыми товарами"""
    return [
        Product("iPhone", "Смартфон", 79990.0, 10),
        Product("Samsung", "Смартфон", 59990.0, 15),
    ]


@pytest.fixture
def sample_products1():
    """Фикстура с образцами товаров"""
    return [
        Product("Телефон", "Смартфон", 50000, 10),
        Product("Планшет", "Графический планшет", 30000, 5),
        Product("Ноутбук", "Игровой ноутбук", 80000, 3),
    ]


@pytest.fixture
def empty_category():
    """Фикстура с пустой категорией"""
    return Category("Пустая", "Нет товаров")


@pytest.fixture
def category_with_products(sample_products1):
    """Фикстура с категорией, содержащей товары"""
    return Category("Электроника", "Техника и гаджеты", sample_products1)
