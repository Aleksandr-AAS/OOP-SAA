from src.LawnGrass import LawnGrass
from src.product import Product


def test_lawngrass_creation():
    """Тест создания газонной травы."""
    print("\n=== Тест создания газонной травы ===")

    grass = LawnGrass(
        name="Газонная трава Premium",
        description="Быстрорастущая газонная трава",
        price=1500.0,
        quantity=50,
        country="Германия",
        germination_period="7-10 дней",
        color="Изумрудный",
    )

    # Проверяем унаследованные атрибуты
    assert (
        grass.name == "Газонная трава Premium"
    ), f"Ожидалось 'Газонная трава Premium', получено {grass.name}"
    assert grass.price == 1500.0, f"Ожидалось 1500.0, получено {grass.price}"

    # Проверяем собственные атрибуты
    assert (
        grass.country == "Германия"
    ), f"Ожидалось 'Германия', получено {grass.country}"
    assert (
        grass.germination_period == "7-10 дней"
    ), f"Ожидалось '7-10 дней', получено {grass.germination_period}"
    assert (
        grass.color == "Изумрудный"
    ), f"Ожидалось 'Изумрудный', получено {grass.color}"

    # Проверяем наследование
    assert isinstance(grass, LawnGrass), "Объект должен быть экземпляром LawnGrass"
    assert isinstance(grass, Product), "LawnGrass должен наследоваться от Product"
