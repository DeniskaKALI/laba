import math

class Opening:
    def __init__(self, width, height):
        self.area = width * height

class Room:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.openings = []

    def add_opening(self, width, height):
        self.openings.append(Opening(width, height))

    def wall_area(self):
        # Общая площадь четырёх стен
        return 2 * self.height * (self.length + self.width)

    def paintable_area(self):
        area = self.wall_area()
        for op in self.openings:
            area -= op.area
        return area

    def required_rolls(self, roll_length, roll_width):
        roll_area = roll_length * roll_width
        return math.ceil(self.paintable_area() / roll_area)
