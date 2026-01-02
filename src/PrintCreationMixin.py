class PrintCreationMixin:
    """Миксин для вывода информации о создании объекта"""

    def __init__(self, *args, **kwargs):
        """Переопределяем __init__ для вывода информации о создании объекта"""
        try:
            # Пытаемся вызвать __init__ родительских классов
            super().__init__(*args, **kwargs)
        except TypeError as e:
            # Если возникает ошибка (например, object.__init__ не принимает аргументы),
            # пробуем вызвать без аргументов
            if "object.__init__" in str(e):
                super().__init__()
            else:
                raise

        # Формируем строку с аргументами
        args_str = ", ".join(repr(arg) for arg in args)

        # Формируем строку с именованными аргументами (если есть)
        kwargs_str = ""
        if kwargs:
            kwargs_str = ", " + ", ".join(
                f"{key}={repr(value)}" for key, value in kwargs.items()
            )

        # Выводим информацию
        print(f"{self.__class__.__name__}({args_str}{kwargs_str})")
