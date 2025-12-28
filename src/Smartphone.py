from src.product import Product


class Smartphone(Product):
    """Класс для представления смартфона, наследуется от Product."""

    def __init__(
        self,
        name,
        description,
        price,
        quantity,
        efficiency: str,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
