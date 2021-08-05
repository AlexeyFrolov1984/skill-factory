box = [
    [' ', 0, 1, 2],
    [0, ' ', ' ', ' '],
    [1, ' ', ' ', ' '],
    [2, ' ', ' ', ' '],
]


def out_box():
    """Функция вывода игрового поля"""
    for i in range(4):
        for j in range(4):
            print(box[i][j], end=" ")
        print()


def check():
    """Функция проверяет кто победил и возращает значение о победителе или ничьей"""
    win = ''
    line = ''
    for i in range(1, 4):
        # Проверка выигрыша по горизонтали
        for j in range(1, 4):
            line += box[i][j]
        if line == 'XXX':
            win = 'КРЕСТИКИ ПОБЕДИЛИ'
        if line == '000':
            win = 'НОЛИКИ ПОБЕДИЛИ'
        line = ''
    for j in range(1, 4):
        # Проверка выигрыша по вертикали
        for i in range(1, 4):
            line += box[i][j]
        if line == 'XXX':
            win = 'КРЕСТИКИ ПОБЕДИЛИ'
        if line == '000':
            win = 'НОЛИКИ ПОБЕДИЛИ'
        line = ''
        # Проверка выигрыша по диагонали
    if box[1][1] == box[2][2] == box[3][3] == 'X' or box[3][1] == box[2][2] == box[1][3] == 'X':
        win = 'КРЕСТИКИ ПОБЕДИЛИ'
    if box[1][1] == box[2][2] == box[3][3] == '0' or box[3][1] == box[2][2] == box[1][3] == '0':
        win = 'НОЛИКИ ПОБЕДИЛИ'
    return win


def play_game():
    """Функция игры - поочередный ввод крестиков и ноликов с проверкой на правильность ввода"""
    rez = ''
    count = 0
    while not rez and count != 9:
        # Ввод координат X и проверка
        coord = input("Введите координаты Х через пробел (х -столбец,  у - строка)")
        while len(coord) != 3 or coord[0] not in '012' or coord[2] not in '012' or coord[1] != ' ':
            print("Что-то ввели не правильно!")
            coord = input("Введите координаты Х через пробел (х -столбец,  у - строка)")
        coord_x = int(coord[2]) + 1
        coord_y = int(coord[0]) + 1
        while box[coord_x][coord_y] != ' ':
            print('Не тупи. Клетка занята. Введи еще раз!')
            coord = input("Введите координаты Х через пробел (х -столбец,  у - строка)")
            coord_x = int(coord[2]) + 1
            coord_y = int(coord[0]) + 1
        box[coord_x][coord_y] = 'X'
        out_box()
        count += 1
        rez = check()
        if not rez and count != 9:
            # Ввод координат 0 и проверка
            coord = input("Введите координаты 0 через пробел (х -столбец,  у - строка)")
            while len(coord) != 3 or coord[0] not in '012' or coord[2] not in '012' or coord[1] != ' ':
                print("Что-то ввели не правильно!")
                coord = input("Введите координаты 0 через пробел (х -столбец,  у - строка)")
            coord_x = int(coord[2]) + 1
            coord_y = int(coord[0]) + 1
            while box[coord_x][coord_y] != " ":
                print('Не тупи. Клетка занята. Введи еще раз!')
                coord = input("Введите координаты 0 через пробел (х -столбец,  у - строка)")
                coord_x = int(coord[2]) + 1
                coord_y = int(coord[0]) + 1
            box[coord_x][coord_y] = '0'
            # Вывод игрового поля после каждого хода
        out_box()
        count += 1
        # Вызов функции проверки победителя
        rez = check()
    # Вывод результата игры на экран
    if not rez:
        print('НИЧЬЯ')
    else:
        print(rez)


out_box()
print('''Добро пожаловать в игру крестики нолики
    Первый игрок ставит крестик на поле, второй нолик путем ввода координат
    Выигрывает игрок, который соберет 3 подряд фигуры по вертикали, горизонтали или диагонали. ПОГНАЛИ!!!''')
play_game()
