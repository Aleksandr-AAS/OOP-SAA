class Product:
    """Класс для представления товара."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __repr__(self):
        """Смотрим объект по ссылке"""
        return f"{self.name}, {self.description}"

    def __str__(self):
        """Возвращает строковое представление товара."""
        return f"{self.description}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Магический метод сложения.
        Возвращает сумму произведений цены на количество у двух объектов.
        Товары можно складывать только из одинаковых классов.
        """
        if type(self) != type(other):
            raise TypeError(
                f"Нельзя складывать товары разных классов. "
                f"Попытка сложить {type(self).__name__} и {type(other).__name__}"
            )

        return (self.price * self.quantity) + (other.price * other.quantity)

    # def __add__(self, other):
    #     """Магический метод сложения.
    #     Возвращает сумму произведений цены на количество у двух объектов.
    #     """
    #     if not isinstance(other, Product):
    #         raise TypeError("Можно складывать только объекты класса Product")
    #
    #     return (self.price * self.quantity) + (other.price * other.quantity)

    @property
    def price(self):
        """Геттер для получения цены"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для установки цены"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict):
        """Добавляет продукт"""
        name = product_data.get("name")
        description = product_data.get("description")
        price = product_data.get("price")
        quantity = product_data.get("quantity")
        return cls(name, description, price, quantity)
