import numpy as np


def game_core_v2(number):
    # Функция уменьшает интервал поиска числа
    count = 1
    predict_2 = 101
    predict_1 = 0
    predict = np.random.randint(1, 101)
    while number != predict:
        count += 1
        if number > predict:
            predict_1 = predict
            predict = np.random.randint(predict_1, predict_2)
        else:
            predict_2 = predict
            predict = np.random.randint(predict_1, predict_2)
    return count


def score_game(game_core):
    # Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core_v2)
