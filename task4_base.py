"""
4) Программа принимает действительное положительное число x и целое
отрицательное число y. Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y). При решении
задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в
степень с помощью оператора возведения в степень. Второй — более сложная
реализация без оператора возведения в степень, предусматривающая использование
цикла.
"""


def check_input_param(x_param, y_param):
    """
    Функция валидации входных параметров
    :param x_param: должно быть действительное положительное число
    :param y_param: должна быть целая отрицательная степень
    :return: либо сообщение о нарушениях в задании входных аргументов и
    возврат False, либо возврат True
    """
    total = None
    if y_param % 1 != 0 or x_param <= 0 or y_param > 0:
        result = ''
        if x_param <= 0:
            result = result + f'\nчисло X не может быть отрицательным, ваше ' \
                              f'число отрицательное X ={x_param}'
        if y_param % 1 != 0:
            result = result + f'\nчисло Y должно быть целым, ваше число не ' \
                              f'целое: Y = {y_param}'
        if y_param > 0:
            result = result + f'\nчисло Y должно быть отрицательным, ваше ' \
                              f'число положительное Y = {y_param}'
        print(result)
        total = False
    else:
        total = True
    return total


def pow_with_operator(x_parameters, y_parameters):
    """
    Функция возведения действительного положительного числа в целую
    отрицатльную степень с помощью оператора **
    :param x_parameters: число
    :param y_parameters: степень
    :return: Возврат значения возведения в степень, либо строка ошибки
    """
    result = None
    if check_input_param(x_parameters, y_parameters):
        y_parameters = int(y_parameters)
        result = x_parameters ** y_parameters
    else:
        result = '\nВходные аргументы не корректны!\n'
    return result


def pow_with_cycle(x_parameters, y_parameters):
    """
    Функция возведения действительного положительного числа в целую
    отрицатльную степень с помощью цикла
    :param x_parameters: число
    :param y_parameters: степень
    :return: Возврат значения возведения в степень, либо строка ошибки
    """
    result = None
    if check_input_param(x_parameters, y_parameters):
        y_param = int(y_parameters)
        mult = 1
        while y_param < 0:
            mult *= 1 / x_parameters
            y_param += 1
        result = mult
    else:
        result = '\nВходные аргументы не корректны!\n'
    return result


first_num = float(input("Введите действительное положительное число x: "))
second_num = float(input("Введите целое отрицательное число y: "))

print(pow_with_operator(first_num, second_num))
print(pow_with_cycle(first_num, second_num))

# проверка
# print(pow(2.3, -3))
# print(pow(4.1, -1))
# print(pow(1.1, -2))
