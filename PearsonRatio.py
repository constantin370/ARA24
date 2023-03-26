#Программа нахождения коеффициента Пирсона!

import math
#Объявление глобальных переменных
data_one = [ ]
data_two = [ ]


def main(data_one: list, data_two: list) -> list:
    """Главная Функция"""
    #Главное меню программы
    print('\nПрограмма нахождения коеффициента Пирсона!\nДля завершения ввода нажмите - (0)\n')
    first_list(data_one)
    second_list(data_two)
    correlation(data_one, data_two)
    
    

def first_list(data_one: list) -> list:
    """Функция заполнения первого списка и вывод результата дисперсии"""
    while True:
        try:
            the_user = float(input('\nВведите данные первого списка: '))
        except ValueError:
            print('\nОшибка ввода! Продолжите заполнения списка!\n')
            continue
        if the_user != 0:
            data_one.append(the_user)
        elif the_user == 0:
            break
        else:
            print('ERROR!')
    print(f'\nПервый список данных равен: {data_one}')


def second_list(data_two: list) -> list: 
    """Функция заполнения второго списка и вывод результата дисперсии"""   
    while True:
        try:
            the_user = float(input('\nВведите данные второго списка: '))
        except ValueError:
            print('\nОшибка ввода! Продолжите заполнения списка!\n')
            continue
        if the_user != 0:
            data_two.append(the_user)
        elif the_user == 0:
            break
        else:
            print('ERROR!')
    print(f'\nВторой список данных равен: {data_two}')


def mean(numbers: list) -> list:
    """ Функция подсчета среднеарефметического значения или метматического ожидания списка"""
    res = 0
    for i in numbers:
        res += i      
    average = res / len(numbers)
    return average


def Deviation_from_the_average_value(numbers: list) -> list:
    """Отклонение от среднего значения data_one и data_two"""
    Deviation_from_the_average_value = 0
    Deviation_from_the_average_value_list = [ ]
    result_mean = mean(numbers)
    for i in numbers:
        Deviation_from_the_average_value = i - result_mean
        Deviation_from_the_average_value_list.append(round(Deviation_from_the_average_value, 2))
    print(f'\nОтклонение от среднего значения списка {numbers} равно: {Deviation_from_the_average_value_list}')
    return Deviation_from_the_average_value_list


def multiplication(numbers: list) -> list:   
    """Функция нахождения значение суммы произведений отклонений средних значений списков data_one и data_two"""
    # (1) - Проверка условия на длину списков!
    if len(data_one) == len(data_two):
        res_1 = Deviation_from_the_average_value(data_one)
        res_2 = Deviation_from_the_average_value(data_two)
        multiplication_of_deviations_list = [ ]
        multiplication_of_deviations = 0
        the_sum_of_the_products_of_deviations = 0
        for i in range(len(res_1)):
            multiplication_of_deviations = res_1[i] * res_2[i]
            multiplication_of_deviations_list.append(round(multiplication_of_deviations, 2))    
            the_sum_of_the_products_of_deviations += multiplication_of_deviations
        print(f'\nПроизведение отклонений средних значений двух списков равны: {multiplication_of_deviations_list} их сумма равна: {round(the_sum_of_the_products_of_deviations, 2)}\n')
    else:
        print(f'''\nОШИБКА: Списки не равны по длинне!\nКолличество эллементов в первом списке равен: {len(data_one)}
Колличество эллементов во втором списке равен: {len(data_two)}''')
        main(data_one, data_two)
    return the_sum_of_the_products_of_deviations
  

def Lets_square_each_deviation_value(numbers: list) -> list:
    """Функция возведения в квадрат каждого отклонения"""
    Deviation_from_the_average_value = 0
    Deviation_from_the_average_value_list = [ ]
    Deviation_from_the_average_value_summ = 0
    result_mean = mean(numbers)
    for i in numbers:
        Deviation_from_the_average_value = (i - result_mean) **2
        Deviation_from_the_average_value_list.append(round(Deviation_from_the_average_value, 2))
        Deviation_from_the_average_value_summ += Deviation_from_the_average_value
    print(f'\nОтклонение  от среднего значения в квадрате равна: {Deviation_from_the_average_value_list} сумма квадратов равна: {round(Deviation_from_the_average_value_summ, 2)}')
    return Deviation_from_the_average_value_summ


def correlation(data_one: list, data_two: list) -> list:
    """Функция расчета коэффициента корреляции Пирсона """
    res_1 = Lets_square_each_deviation_value(data_one)
    res_2 = Lets_square_each_deviation_value(data_two)
    res_3 = multiplication(Deviation_from_the_average_value)
    try:
        decision = res_3 / (math.sqrt(res_1 * res_2))
    except ZeroDivisionError:
        print('Ошибка: На нуль делить нельзя!')
        main(data_one, data_two)
    #(1) - Проверка по условию диапозонов значения коэффциента    
    if decision >= 0.75:
        print(f'\nЕсть Корреляция!\nЗначение коэффициента корреляции Пирсона составило {round(decision, 2)},\nчто соответствует весьма высокой тесноте связи между {data_one} и {data_two}\n')
    elif decision <= -0.75:
        print(f'\nЕсть обратная Корреляция!\nЗначение коэффициента корреляции Пирсона составило {round(decision, 2)},\nчто соответствует низкой тесноте связи между {data_one} и {data_two}\n')
    else:
        print(f'У списков {data_one} и {data_two} отсутвует кореляция коэффициент равен: {round(decision, 2)}\n')
    return decision


if __name__ == "__main__":
    main(data_one, data_two)