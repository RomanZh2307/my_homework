def check_winner():
    if area[0][0] == "X" and area[0][1] == "X" and area[0][2] == "X":
        return "X"
    if area[1][0] == "X" and area[1][1] == "X" and area[1][2] == "X":
        return "X"
    if area[2][0] == "X" and area[2][1] == "X" and area[2][2] == "X":
        return "X"
    return "*"


def draw_area():
    for i in area:
        print(*i)
    print()


area = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
print("добро пожаловать в крестики-нолики")
print("----------------------------------")
draw_area()
# area[0][0] = "X"
for turn in range(1, 10):
    print(f"Ход: {turn}")
    if turn % 2 == 0:
        turn_char = "0"
        print("Ходят нолики")
    else:
        turn_char = "X"
        print("Ходят крестки")
    row = int(input("Введите номер строки (1,2,3)")) - 1
    column = int(input("Введите номер столбца (1,2,3)")) - 1
    if area[row][column] == "*":
        area[row][column] = turn_char
    else:
        print("Ячейка уже занята, вы пропускаете ход")
        continue

    draw_area()

    if check_winner() == "X":
        print("Победа крестиков")
        break
    if check_winner() == "0":
        print("Победа ноликов")
        break
    if check_winner() == "*" and turn == 9:
        print("Ничья")
        break
