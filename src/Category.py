from src.product import Product


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
        # self.__products = []
        self.__products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    # def add_product(self, product):
    #     """Добавляем количество по категориям"""
    #     self.__products.append(product)
    #     Category.product_count += 1

    def add_product(self, product):
        """
        Добавляет продукт в категорию.

        Args:
            product: Объект класса Product или его наследников

        Raises:
            TypeError: Если переданный объект не является Product или наследником
        """
        # Используем isinstance() для проверки наследования
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты класса Product или его наследников"
            )

        self.__products.append(product)
        print(f"Продукт '{product.name}' добавлен в категорию '{self.name}'")

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
