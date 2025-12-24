class Category:
    """Класс для представления категорий товара."""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, product):
        """Добавляем количество по категориям"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер  продукт"""
        prod_str = ""
        for prod in self.__products:
            prod_str += f"{prod.name},{prod.price} руб. Остаток: {prod.quantity} шт.\n"
        return prod_str

    def __str__(self):
        """Возвращает строковое представление категории с общим количеством товаров."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.description}, {total_quantity} шт."

#     """Возвращает строковое представление категории."""
#     return f"{self.description}, {len(self.__products)} шт."
