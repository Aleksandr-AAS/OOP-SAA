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

    def middle_price(self):
        """
        Рассчитывает средний ценник всех товаров в категории.
        Если в категории нет товаров или сумма делится на ноль, возвращает 0.
        """
        try:
            # Суммируем все цены товаров
            total_price = sum(product.price for product in self.__products)
            # Получаем количество товаров
            total_count = len(self.__products)
            # Вычисляем среднюю цену
            average = total_price / total_count
            return round(average, 2)

        except ZeroDivisionError:
            # Обрабатываем случай, когда в категории нет товаров
            return 0
