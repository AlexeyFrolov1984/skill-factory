box = [
    [' ', 0, 1, 2],
    [0, ' ', ' ', ' '],
    [1, ' ', ' ', ' '],
    [2, ' ', ' ', ' '],
]
count = 0
rez = ''


def out_box():
    for i in range(4):
        for j in range(4):
            print(box[i][j], end=" ")
        print()


# Функция проверки выигрыша
def check():
    win = ''
    line = ''
    for i in range(1, 4):
        for j in range(1, 4):
            line += box[i][j]
        if line == 'XXX':
            win = 'КРЕСТИКИ ПОБЕДИЛИ'
        if line == '000':
            win = 'НОЛИКИ ПОБЕДИЛИ'
        line = ''
    for j in range(1, 4):
        for i in range(1, 4):
            line += box[i][j]
        if line == 'XXX':
            win = 'КРЕСТИКИ ПОБЕДИЛИ'
        if line == '000':
            win = 'НОЛИКИ ПОБЕДИЛИ'
        line = ''
    if box[1][1] == box[2][2] == box[3][3] == 'X' or box[3][1] == box[2][2] == box[1][3] == 'X':
        win = 'КРЕСТИКИ ПОБЕДИЛИ'
    if box[1][1] == box[2][2] == box[3][3] == '0' or box[3][1] == box[2][2] == box[1][3] == '0':
        win = 'НОЛИКИ ПОБЕДИЛИ'
    return win


out_box()
while not rez and count != 9:
    # Ввод координат X и проверка
    coordinate = input("Введите координаты Х через пробел (х у)")
    coordinate_x = int(coordinate[2]) + 1
    coordinate_y = int(coordinate[0]) + 1
    while box[coordinate_x][coordinate_y] != ' ':
        print('Не тупи. Клетка занята. Введи еще раз!')
        coordinate = input("Введите координаты Х через пробел (х у)")
        coordinate_x = int(coordinate[2]) + 1
        coordinate_y = int(coordinate[0]) + 1
    box[coordinate_x][coordinate_y] = 'X'
    out_box()
    count += 1
    check()
    rez = check()
    # Ввод координат 0 и проверка
    if not rez and count != 9:
        coordinate = input("Введите координаты 0 через пробел (х у)")
        coordinate_x = int(coordinate[2]) + 1
        coordinate_y = int(coordinate[0]) + 1

        while box[coordinate_x][coordinate_y] != " ":
            print('Не тупи. Клетка занята. Введи еще раз!')
            coordinate = input("Введите координаты 0 через пробел (х у)")
            coordinate_x = int(coordinate[2]) + 1
            coordinate_y = int(coordinate[0]) + 1
        box[coordinate_x][coordinate_y] = '0'
        out_box()
        count += 1
        check()
        rez = check()
if not rez:
    print('НИЧЬЯ')
else:
    print(rez)
