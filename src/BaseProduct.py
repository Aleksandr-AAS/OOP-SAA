from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов"""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Абстрактный конструктор продукта
        """
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """Абстрактный метод строкового представления для отладки"""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод строкового представления для пользователя"""
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        """Абстрактный геттер для получения цены"""
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float) -> None:
        """Абстрактный сеттер для установки цены"""
        pass

    @abstractmethod
    def __add__(self, other: Any) -> float:
        """
        Абстрактный метод сложения товаров
        """
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_data: Dict[str, Any]) -> "BaseProduct":
        """
        Абстрактный классовый метод для создания нового продукта
        """
        pass
