from src.Category import Category


def test_category_creation(sample_products):
    """Тест создания категории"""
    category = Category("Смартфоны", "Описание", sample_products)

    assert category.name == "Смартфоны"
    assert category.description == "Описание"
    assert len(category.products) == 73
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_category_empty_products():
    """Тест создания категории без товаров"""
    category = Category("Ноутбуки", "Описание")

    assert category.name == "Ноутбуки"
    assert category.products == ""
    assert Category.category_count == 2
    assert Category.product_count == 2


def test_none_products_list():
    """Тест с явным указанием None в products"""
    category = Category("Категория", "Описание", None)
    assert category.products == ""
