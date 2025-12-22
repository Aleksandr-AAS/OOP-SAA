import pytest
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
from src.product import Product


@pytest.fixture
def sample_products():
    """Фикстура с тестовыми товарами"""
    return [
        Product("iPhone", "Смартфон", 79990.0, 10),
        Product("Samsung", "Смартфон", 59990.0, 15),
    ]
