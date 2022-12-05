"""
1) Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль.
"""
def get_division(numerator, denominator):
    """
    Функция деления двух чисел
    :param numerator: Числитель
    :param denominator: Знаменатель
    :return: результат выполнения деления или, в случае равенства знаменателя
    нулю, возврат поясняющего сообщения
    """
    if denominator == 0:
        return "Знаменатель не может быть равен нулю"
    return numerator / denominator
def get_division_v2(numerator, denominator):
    """
     Функция деления двух чисел
    :param numerator: Числитель
    :param denominator: Знаменатель
    :return: результат выполнения деления или, в случае равенства знаменателя
    нулю, выбрасываем ошибку
    """
    try:
        result = numerator / denominator
    except ValueError:
        return 'Value Error'
    except ZeroDivisionError:
        return 'Вы не можете делить на ноль!'
    return result


number_1 = int(input("Введите первое число (числитель): "))
number_2 = int(input("Введите второе число (знаменатель): "))

print(get_division(number_1, number_2))
print(get_division_v2(number_1, number_2))
