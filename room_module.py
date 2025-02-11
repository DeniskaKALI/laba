"""
Модуль room_module

Данный модуль содержит классы для расчёта площади стен комнаты, которые подлежат
оклейке обоями, с учётом исключаемых элементов (окон и дверей), а также определяет 
количество необходимых рулонов обоев.
"""

import math

class Opening:
    """
    Класс Opening представляет элемент (например, окно или дверь), площадь которого 
    не подлежит оклейке обоями.

    Атрибуты:
        area (float): Площадь элемента, вычисляемая как произведение ширины на высоту.
    """
    def __init__(self, width, height):
        """
        Инициализация объекта Opening.

        Параметры:
            width (float): Ширина элемента.
            height (float): Высота элемента.
        """
        self.area = width * height

class Room:
    """
    Класс Room описывает комнату и предоставляет методы для расчёта площади стен, 
    подлежащих оклейке обоями, с вычитанием площади исключаемых элементов.

    Атрибуты:
        length (float): Длина комнаты.
        width (float): Ширина комнаты.
        height (float): Высота комнаты.
        openings (list): Список объектов класса Opening, представляющих исключаемые элементы.
    """
    def __init__(self, length, width, height):
        """
        Инициализация объекта Room с заданными размерами.

        Параметры:
            length (float): Длина комнаты.
            width (float): Ширина комнаты.
            height (float): Высота комнаты.
        """
        self.length = length
        self.width = width
        self.height = height
        self.openings = []

    def add_opening(self, width, height):
        """
        Добавляет объект класса Opening (например, окно или дверь) в список исключаемых элементов.

        Параметры:
            width (float): Ширина элемента.
            height (float): Высота элемента.
        """
        self.openings.append(Opening(width, height))

    def wall_area(self):
        """
        Вычисляет общую площадь четырёх стен комнаты.

        Формула:
            2 * высота * (длина + ширина)

        Возвращает:
            float: Полная площадь стен комнаты.
        """
        return 2 * self.height * (self.length + self.width)

    def paintable_area(self):
        """
        Вычисляет площадь стен, подлежащую оклейке обоями.

        От полной площади стен отнимается суммарная площадь всех исключаемых элементов.

        Возвращает:
            float: Площадь стен, которую нужно оклеить.
        """
        area = self.wall_area()
        for op in self.openings:
            area -= op.area
        return area

    def required_rolls(self, roll_length, roll_width):
        """
        Определяет количество рулонов обоев, необходимых для оклейки стен.

        Параметры:
            roll_length (float): Длина рулона обоев.
            roll_width (float): Ширина рулона обоев.

        Возвращает:
            int: Количество рулонов, необходимых для покрытия вычисленной площади.
        """
        roll_area = roll_length * roll_width
        return math.ceil(self.paintable_area() / roll_area)
