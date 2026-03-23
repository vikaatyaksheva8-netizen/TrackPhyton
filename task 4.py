if __name__ == "__main__":
    class Vehicle:
        """
        Базовый класс для представления транспортного средства.

        Класс описывает общие свойства любого транспортного средства:
        марку, модель, год выпуска и состояние двигателя.
        """
    
        def __init__(self, brand: str, model: str, year: int):
            """
            Создание и подготовка к работе объекта "Транспортное средство".

            :param brand: Марка транспортного средства.
            :param model: Модель транспортного средства.
            :param year: Год выпуска транспортного средства.
            :raises TypeError: Если brand или model не являются строкой,
                либо year не является целым числом.
            :raises ValueError: Если brand или model являются пустой строкой,
                либо year имеет некорректное значение.
            """
            if not isinstance(brand, str):
                raise TypeError("Марка транспортного средства должна быть строкой")
            if not brand.strip():
                raise ValueError("Марка транспортного средства не может быть пустой")
            self.brand = brand.strip()

            if not isinstance(model, str):
                raise TypeError("Модель транспортного средства должна быть строкой")
            if not model.strip():
                raise ValueError("Модель транспортного средства не может быть пустой")
            self.model = model.strip()

            if not isinstance(year, int):
                raise TypeError("Год выпуска должен быть целым числом")
            if year <= 0:
                raise ValueError("Год выпуска должен быть положительным числом")
            self.year = year

            self._engine_started = False

        def __str__(self) -> str:
            """
            Возвращает строковое представление транспортного средства.

            :return: Строка в удобочитаемом формате с основной информацией
                о транспортном средстве.
            """
            engine_status = "запущен" if self._engine_started else "выключен"
            return f"{self.brand} {self.model} ({self.year}), двигатель: {engine_status}"

        def __repr__(self) -> str:
            """
            Возвращает техническое строковое представление объекта.

            :return: Строка с именем класса и значениями основных атрибутов,
                удобная для отладки.
            """
            return (
                f"Vehicle(brand='{self.brand}', "
                f"model='{self.model}', "
                f"year={self.year})"
            )

        def start_engine(self) -> bool:
            """
            Запускает двигатель транспортного средства.

            :return: True, если двигатель был успешно запущен;
                False, если двигатель уже был запущен.
            """
            ...

        def stop_engine(self) -> bool:
            """
            Останавливает двигатель транспортного средства.

            :return: True, если двигатель был успешно остановлен;
                False, если двигатель уже был выключен.
            """
            ...

        def move(self, distance: float) -> str:
            """
            Выполняет движение транспортного средства на указанное расстояние.

            :param distance: Расстояние, которое должно проехать транспортное средство, в километрах.
            :return: Сообщение о результате движения транспортного средства.
            :raises TypeError: Если distance не является числом.
            :raises ValueError: Если distance меньше или равно нулю.
            """
            ...


    class Truck(Vehicle):
        """
        Дочерний класс для представления грузового автомобиля.

        Класс наследует общие свойства транспортного средства
        и дополняет их грузоподъёмностью.
        """

        def __init__(self, brand: str, model: str, year: int, load_capacity: float):
            """
            Создание и подготовка к работе объекта "Грузовой автомобиль".

            :param brand: Марка грузового автомобиля.
            :param model: Модель грузового автомобиля.
            :param year: Год выпуска грузового автомобиля.
            :param load_capacity: Грузоподъёмность автомобиля в тоннах.
            :raises TypeError: Если load_capacity не является числом.
            :raises ValueError: Если load_capacity меньше или равна нулю.
            """
            super().__init__(brand, model, year)

            if not isinstance(load_capacity, (int, float)):
                raise TypeError("Грузоподъёмность должна быть числом")
            if load_capacity <= 0:
                raise ValueError("Грузоподъёмность должна быть положительным числом")
            self.load_capacity = float(load_capacity)

        def __str__(self) -> str:
            """
            Возвращает строковое представление грузового автомобиля.

            :return: Строка в удобочитаемом формате с основной информацией
                о грузовом автомобиле.
            """
            engine_status = "запущен" if self._engine_started else "выключен"
            return (
                f"{self.brand} {self.model} ({self.year}), "
                f"грузоподъёмность: {self.load_capacity} т, "
                f"двигатель: {engine_status}"
            )

        def __repr__(self) -> str:
            """
            Возвращает техническое строковое представление объекта.

            :return: Строка с именем класса и значениями основных атрибутов
                грузового автомобиля.
            """
            return (
                f"Truck(brand='{self.brand}', "
                f"model='{self.model}', "
                f"year={self.year}, "
                f"load_capacity={self.load_capacity})"
            )

        def move(self, distance: float) -> str:
            """
            Выполняет движение грузового автомобиля на указанное расстояние.

            Метод перегружен, потому что для грузового автомобиля важно
            учитывать, что он используется не просто для передвижения,
            а для перевозки грузов.

            :param distance: Расстояние, которое должен проехать грузовой автомобиль, в километрах.
            :return: Сообщение о результате движения грузового автомобиля.
            :raises TypeError: Если distance не является числом.
            :raises ValueError: Если distance меньше или равно нулю.
            """
            ...

        def load_cargo(self, weight: float) -> bool:
            """
            Выполняет загрузку груза в автомобиль.

            :param weight: Масса груза в тоннах.
            :return: True, если груз может быть загружен;
                False, если масса груза превышает грузоподъёмность автомобиля.
            :raises TypeError: Если weight не является числом.
            :raises ValueError: Если weight меньше или равен нулю.
            """
            ...
    pass