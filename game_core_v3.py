import numpy as np

number = np.random.randint(1, 101) # Загадываем число от 1 до 100

def game_core_v3(number)  -> int:
    """Сначала предполагаем, что загаданное число равно 10, если предполагаемое
    число меньше загаданного, то увеличиваем его на 10. Таким образом мы находим
    десяток, в котором находится загаданное число. Далее если предполагаемое число
    меньше загаданного, мы уменьшаем его на 1. Таким образом мы определяем
    загаданное число в найденном десятке.
       Функция принимает загаданное число и возвращает число попыток
       
    Args:
        number (int): Загаданное число от 1 до 100.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = 10 # Изначально предполагаем, что загаданное число 10
    
    while number != predict:
        count += 1
        if number > predict: # Определяем в каком десятке находится загаданное число
            predict += 10
        elif number < predict: # Определяем число в десятке
            predict -= 1

    return count


def score_game(game_core_v3) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        game_core_v3 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

score_game(game_core_v3)