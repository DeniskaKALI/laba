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
        # Total area of the four walls
        return 2 * self.height * (self.length + self.width)

    def paintable_area(self):
        area = self.wall_area()
        for op in self.openings:
            area -= op.area
        return area

    def required_rolls(self, roll_length, roll_width):
        roll_area = roll_length * roll_width
        return math.ceil(self.paintable_area() / roll_area)

print("Enter room dimensions:")
room_length = float(input("Length: "))
room_width = float(input("Width: "))
room_height = float(input("Height: "))

room = Room(room_length, room_width, room_height)

if input("Are there any windows or doors to exclude from wallpapering? (yes/no): ").lower() == "yes":
    while True:
        op_width = float(input("Opening width: "))
        op_height = float(input("Opening height: "))
        room.add_opening(op_width, op_height)
        another = input("Add another opening? (yes/no): ").lower()
        if another != "yes":
            break

print("Enter wallpaper roll dimensions:")
roll_length = float(input("Roll length: "))
roll_width = float(input("Roll width: "))

print("Total area to be wallpapered:", room.paintable_area())
print("Number of wallpaper rolls needed:", room.required_rolls(roll_length, roll_width))