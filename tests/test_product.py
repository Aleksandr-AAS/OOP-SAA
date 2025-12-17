from src.product import Product


def test_product_creation():
    """Тест создания товара"""
    product = Product(
        name="iPhone 13",
        description="Смартфон Apple",
        price=79990.0,
        quantity=10
    )

    assert product.name == "iPhone 13"
    assert product.description == "Смартфон Apple"
    assert product.price == 79990.0
    assert product.quantity == 10
