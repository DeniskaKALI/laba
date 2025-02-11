from room_module import Room

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
