"""
6) Реализовать функцию int_func(), принимающую слово из маленьких латинских
букв и возвращающую его же, но с прописной первой буквой. Например,
print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной
буквы. Необходимо использовать написанную ранее функцию int_func().
"""


# def int_func(word):
#     print(word.title())
#
# string = input("Введите слово: ")
# int_func(string)

def int_func_single(word):
    """
    Функция для преобразования одного слова
    :param word: слово
    :return: слово с большой буквы
    """
    index = 0
    result = ''
    while index < len(word):
        if index == 0:
            result += word[index].upper()
        else:
            result += word[index]
        index += 1
    return result


# Функция для строки, без использования int_func_single
# def int_func_each(string):
#     index = 0
#     result = ''
#     while index < len(string):
#         if index == 0:
#             result += string[index].upper()
#         elif string[index - 1] == ' ':
#             result += string[index].upper()
#         else:
#             result += string[index]
#         index += 1
#     return result

def int_func_each(string):
    """
    Функция для преобразования строки
    :param string: строка неотформатированная
    :return: строка отформатированная (первые буквы каждого слова переведены
    в верхний регистр)
    """
    temp = string.split(' ')
    index = 0
    result = []
    while index < len(temp):
        word = int_func_single(temp[index])
        result.append(word)
        index += 1
    return " ".join(result)


one_word = input("Введите слово маленькими буквами: ")
print(int_func_single(one_word))

my_string = input("Введите строку маленькими буквами: ")
print(int_func_each(my_string))
