from src.Smartphone import Smartphone
from src.product import Product


def test_smartphone_creation():
    """Тест создания смартфона."""
    print("\n=== Тест создания смартфона ===")

    phone = Smartphone(
        name="Apple iPhone",
        description="Флагманский смартфон",
        price=89990.0,
        quantity=15,
        efficiency="Apple A16 Bionic",
        model="iPhone 14 Pro",
        memory=256,
        color="Deep Purple",
    )

    # Проверяем унаследованные атрибуты
    assert (
        phone.name == "Apple iPhone"
    ), f"Ожидалось 'Apple iPhone', получено {phone.name}"
    assert phone.price == 89990.0, f"Ожидалось 89990.0, получено {phone.price}"

    # Проверяем собственные атрибуты
    assert (
        phone.efficiency == "Apple A16 Bionic"
    ), f"Ожидалось 'Apple A16 Bionic', получено {phone.efficiency}"
    assert (
        phone.model == "iPhone 14 Pro"
    ), f"Ожидалось 'iPhone 14 Pro', получено {phone.model}"
    assert phone.memory == 256, f"Ожидалось 256, получено {phone.memory}"
    assert (
        phone.color == "Deep Purple"
    ), f"Ожидалось 'Deep Purple', получено {phone.color}"

    # Проверяем наследование
    assert isinstance(phone, Smartphone), "Объект должен быть экземпляром Smartphone"
    assert isinstance(phone, Product), "Smartphone должен наследоваться от Product"
