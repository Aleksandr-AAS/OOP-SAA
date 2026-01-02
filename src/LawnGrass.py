from src.product import Product


class LawnGrass(Product):
    """Класс для представления газонной травы, наследуется от Product."""

    def __init__(
        self,
        name,
        description,
        price,
        quantity,
        country: str,
        germination_period: str,
        color: str,
    ):
        """
        Инициализация газонной травы
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
