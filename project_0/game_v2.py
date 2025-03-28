"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""
# Импортируем библиотеки numpy
import numpy as np


def random_predict(number: int = 1) -> int:

    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Определение переменных: счетчик попыток, минимальное и максимальное возможные числа
    count = 0
    min_number = 1
    max_number = 100
    predict_number = int((max_number + min_number) // 2) # первое редполагаемое число 
    # Цикл для определения загаданного числа
    while True:
        count += 1
        if number < predict_number:
            max_number = predict_number - 1
            predict_number = (max_number + min_number) // 2
        elif number > predict_number:
            min_number = predict_number + 1
            predict_number = (max_number + min_number) // 2
        else:
            break  # выход из цикла если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    # Переменная со списком колличества попыток
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел
    # Цикл по списку чисел угадываем каждое число
    for number in random_array:
        count_ls.append(random_predict(number))
    # Переменная со средним значением количества попыток
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
