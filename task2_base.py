"""
2) Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод
данных о пользователе одной строкой.
"""
def show_user_data(name, surname, birth, city, email, phone):
    """
    Функция выводит данные о пользователе одной строкой
    :param name: имя пользователя
    :param surname: фамилия пользователя
    :param birth: дата рождения
    :param city: город проживания
    :param email: электронная почта
    :param phone: номер телефона
    :return: вывод на экран данных
    """
    #Ввыводим, как написано в задании, одной строкой без переноса?
    print(f'Имя: {name}, фамилия: {surname}, дата рождения: {birth}, город '
          f'проживания: {city}, email: {email}, телефон: {phone}')

user_name = input("Введите имя пользователя: ")
user_surname = input("Введите фамилию пользователя: ")
user_birth = input("Введите дату рождения пользователя: ")
user_city = input("Введите город проживания пользователя: ")
user_email = input("Введите эл. почту пользователя: ")
user_phone = input("Введите номер телефона пользователя: ")

show_user_data(name=user_name,
               birth=user_birth,
               email=user_email,
               city=user_city,
               surname=user_surname,
               phone=user_phone)
