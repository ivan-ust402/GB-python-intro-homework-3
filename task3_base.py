"""
3) Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""
def my_func(num_1, num_2, num_3):
    """
    Функция нахождения суммы двух наибольших аргументов
    :param num_1: первое число
    :param num_2: второе число
    :param num_3: третье число
    :return: сумма двух наибольших аргументов
    """
    num_sum = None
    if num_1 < num_2 < num_3 or num_1 < num_3 < num_2:
        num_sum = num_2 + num_3
    elif num_2 < num_1 < num_3 or num_2 < num_3 < num_1:
        num_sum = num_1 + num_3
    elif num_3 < num_1 < num_2 or num_3 < num_2 < num_1:
        num_sum = num_1 + num_2
    return num_sum

# Для тестирования
# while input("Хотите ввести аргументы. Введите 'да': ") == "да":
#     first_arg = int(input("Введите первое число: "))
#     second_arg = int(input("Введите второе число: "))
#     third_arg = int(input("Введите третье число: "))
#     sum_args = my_func(first_arg, second_arg, third_arg)
#     print(f'Сумма двух наибольших из введенных чисел: {sum_args}')

first_arg = int(input("Введите первое число: "))
second_arg = int(input("Введите второе число: "))
third_arg = int(input("Введите третье число: "))
sum_args = my_func(first_arg, second_arg, third_arg)
print(f'Сумма двух наибольших из введенных чисел: {sum_args}')
