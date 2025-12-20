from src.product import Product


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
