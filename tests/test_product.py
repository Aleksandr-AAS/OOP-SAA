from src.product import Product
from src.Smartphone import Smartphone


def test_product_creation():
    """Тест создания товара"""
    product = Product(
        name="iPhone 13", description="Смартфон Apple", price=79990.0, quantity=10
    )
    assert product.name == "iPhone 13"
    assert product.description == "Смартфон Apple"
    assert product.price == 79990.0
    assert product.quantity == 10


def test_new_product():
    product1 = Product.new_product(
        {"name": "Телефон", "description": "Смартфон", "price": 30000, "quantity": 10}
    )
    assert product1.name == "Телефон"
    assert product1.price == 30000
    assert isinstance(product1, Product)


def test_product_addition():
    """Тест сложения товаров"""
    # Одинаковые классы
    p1 = Product("Товар1", "Описание", 100, 2)
    p2 = Product("Товар2", "Описание", 200, 3)
    assert p1 + p2 == 800  # 100*2 + 200*3 = 800

    # Разные классы - должна быть ошибка
    s = Smartphone("Смартфон", "Описание", 500, 1, 95.5, "Model", 256, "Black")
    try:
        p1 + s
        assert False, "Ожидалась ошибка для разных классов"
    except TypeError:
        pass
