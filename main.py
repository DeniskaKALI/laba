"""
Скрипт main.py

Скрипт осуществляет взаимодействие с пользователем для ввода размеров комнаты, 
исключаемых элементов (окон/дверей) и размеров рулона обоев, а затем с помощью 
модуля room_module производит расчёт:
    - Площади стен, подлежащих оклейке.
    - Количества необходимых рулонов обоев.
"""

from room_module import Room

def main():
    """
    Основная функция скрипта, реализующая пользовательский интерфейс.
    """
    print("Enter room dimensions:")
    room_length = float(input("Length: "))
    room_width = float(input("Width: "))
    room_height = float(input("Height: "))

    room = Room(room_length, room_width, room_height)

    # Проверка наличия окон или дверей, которые не требуется оклеивать обоями
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

    # Вывод результатов расчётов
    print("Total area to be wallpapered:", room.paintable_area())
    print("Number of wallpaper rolls needed:", room.required_rolls(roll_length, roll_width))

if __name__ == "__main__":
    main()
