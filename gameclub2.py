#Программа игры: $$$_Игровой клуб_$$$ version 1.0

# Установить и импортировать библиотеку pyfiglet для красивого вывода в консоль
# Для коректной работы игровых функций следует импортировать модули random, time
# Установить и импортировать библиотеку colorama с целью изменить цвета выводимого текста на экран 
# ('\033[33m' +) -> это означает смена цвета текста

from pyfiglet import Figlet
import random
import time
from colorama import *
init()


def main(): 
    loading()

    #Главное меню программы 
    text = Figlet(font="slant",  width=150)
    print(text.renderText("Welcome to the gaming club"))

    #print('\n', '\033[36m'+ 'Welcome to the gaming club\n')
    #Проверка пользователя на предмет финансовой состоятельности 
    cash = Check_Data_1(input('\033[36m'+ 'Внесите деньги! Минимальный депозит 100 рублей: '))
    loading()

    while cash >= 100:
        #Выбор из списка игр пользователем
        the_user = input('\033[36m'+ '''Список доступных игр:\n(1) - Отгадай число 
(2) - Игровой автомат\n(3) - Выход\n''')

        if the_user == '1': 
            loading()
            print('\033[33m' + 'Каждая поптыка будет стоить Вам  20 рублей! В случае проигрыша с вашего счета спишется 20 рублей!\n')
            roulette(cash)
        elif the_user == '2':
            loading()
            print('\033[33m' + '''\nAttention Please: Перед началом игры ознакомьтесь с правилами: 
(1) - Все числа на экране должны совпасть
(2) - Каждая поптыка будет стоить Вам  20 рублей! В случае проигрыша с вашего счета спишется 20 рублей!
(3) - Если первая попытка оказалась удачной: Выгрышь будет равен половине вашего депозита! 
      Если нет, то последующие Выйгрыши будут равны половине от его остатка!''')
            slot_machine(cash)
        elif the_user == '3':
            print(Style.RESET_ALL + '\nВы вышли из программы! Возврат депозита в размере: ', cash, 'рублей')
            time.sleep(5)
            exit()
        else:
            print(Style.RESET_ALL + '\nERROR: Ошибка ввода! Возврат депозита в размере: ', cash, 'рублей')
            time.sleep(5)
            exit() 
    else:
        print(Style.RESET_ALL + '\nБомжуй от сюда!')
        time.sleep(5)
        exit()


def roulette(cash: float) -> float:
    """Фнкция игры: Угадай число"""
    #Объявляем переменные функции импортируем модуль random для коректной работы функции
    secret = random.randint(1, 10)
    counter = 0
    
    while cash > 20:
        #Локальной меню пользователя 
        the_user = input(Style.RESET_ALL + '\n(1) - Начать игру (2) - Выход\n' )

        if the_user == '1':
            for i in range(1, 3 + 1):
                #В целях корректной работы функции было принято решение локально внутри самой функции 
                #обработать исключение связанное с вводом данных от пользователя! Данный вариат позволят вернуть денежные средства внесенные 
                #пользователем не прерывая работу всей программы и сделать откат в начало функции roulette на случай ошибки ValueError...
                try:
                    user = input('\nОТГАДАЙ ЧИСЛО ОТ 1 до 10: ')
                    user = int(user)
                except ValueError:
                    print('\n_ERROR_:\nВы ввели не число! Попробуйте еще раз!\n')
                    roulette(cash)

                if user > secret:
                    counter = counter + 1
                    print('\n', user, 'число больше чем нужно, пробуйте еще раз', 'использовали', i, 'попытоку.\n')
                    continue
                elif user < secret:
                    counter = counter + 1
                    print('\nзагаданное число', user, 'меньше чем нужно, пробуйте еще раз', 'использовали', i, 'попытоку\n')
                    continue
                else:
                    counter = counter + 1
                    cash += 20
                    print('\nВЫ УГАДАЛИ ЧИСЛО:',  secret, 'ПОЗДРАВЛЯЕМ!!!! ЧИСЛО ИСПОЛЬЗОВАННЫХ ПОПЫТОК\n',counter, 'ВАШ ВЫЙГРЫШЬ СОСТАВИЛ', cash, 'РУБЛЕЙ\n')
                    roulette(cash)
            else:
                cash -= 20
                print('\nВы проиграли! Ваш баланс:', cash, 'рублей')
                roulette(cash)
        elif the_user == '2':
            print('\nВаш выйгрышь составил: ', cash, 'рублей')
            time.sleep(3)
            exit()
        else:
            print('\n_ERROR_:\nОшибка ввода! Попробуйте еще раз!\n')
            time.sleep(2)
            roulette(cash)
    else:
        print('\nКончились деньги')
        main()


def slot_machine(cash: float) -> float:
    """Функция игры: Иговой автомат!"""
    #Объявляем переменные функции импортируем модуль random для коректной работы функции
    slot_one = random.randint(1, 3)
    slot_two = random.randint(1, 3)
    slot_three = random.randint(1, 3)
    

    #Локальное меню пользователя
    the_user = input(Style.RESET_ALL + '\n(1) - Дернуть рубильник\n(2) - Выход\n')

    #Провекра условий по меню 
    while cash >= 20:
        if the_user == '1':
            if slot_one == slot_two == slot_three:
                loading()
                cash += cash / 2
                print(Style.RESET_ALL + '\nПобеда', slot_one, slot_two, slot_three, cash)
                slot_machine(cash)
            else:
                loading() 
                cash -= 20
                print(Style.RESET_ALL + '', slot_one, slot_two, slot_three, cash, 'Проигрышь', sep='\n')
                slot_machine(cash)
        elif the_user == '2':
            print('\nВаш выйгрышь составил: ', cash, 'рублей')
            time.sleep(3)
            exit()
        else:
            print('\n_ERROR_:\nОшибка ввода данных! Попробуйте еще раз')
            slot_machine(cash)
    else:
        print('\nНедостаточно средств:\nСумма сдачи составила', cash, 'рублей')
        main()
    
    
def Check_Data_1(num: str) -> float:
    """Функция проверки и перевода данных c str во float"""
    try: 
        num = float(num)
        return num
    except ValueError:
        print(Style.RESET_ALL + '\n_ERROR_:\nВы ввели не число!\nПопробуйте еще раз!\n', '\n')
        main()

       
def loading() -> None:
    """Функция вывода (показа) загрузочного процесса на экран"""
    replay = 3
    for i in range(1, replay + 1):
        print('\n', '\t', ' ' * (replay-i) + '\033[33m' + '$' * i + '\033[32m' + '_ Загрузка_', '\033[33m' + '$' * i, '\n')
        time.sleep(0.7)
    print()


if __name__ == "__main__":
    main()



