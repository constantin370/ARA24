#from libratTwo import ROE Check_Data_One, Check_Data_Two
from pyfiglet import Figlet

# Обявление переменных
return_on_equity_ratio = 0
clear_profit_sum = 0 #Чистая прибыль
revenue_sum = 0 #Выручка
Assets_at_the_last_reporting_date_sum = 0 #Активы на последнюю отчетную дату
own_capital_sum = 0 #Собственный капитал

def main(clear_profit_sum, revenue_sum, Assets_at_the_last_reporting_date_sum, own_capital_sum):
    # Красивый ввод на консоль
    text = Figlet(font="slant",  width=200)
    print(text.renderText("DuPont Model"))
    print("\nDuPont Model\n")
    # Главное меню программы
    control_panel = Check_Data_One(input('Выберите операцию:\n(1) - Модель Дюпона\n(2) - Выход\n'))

    if control_panel == 1:
        while True:
            #Чистая прибыль
            clear_profit = Check_Data_Two(input('Введите Чистую прибыль: '))
            #Выручка
            revenue = Check_Data_Two(input('Введите Выручку: '))
            #Активы на последнюю отчетную дату
            Assets_at_the_last_reporting_date = Check_Data_Two(input('Введите Активы на последнюю отчетную дату: '))
            #Собственный капитал
            own_capital = Check_Data_Two(input('Введите Собственный капитал: '))
            # Завершить ввод данных или продолжить
            the_user = input("\nЗавершить ввод данных?\n (Y)-Да\n (N)-Нет\n")

            # Условие для проверки завершен ввод даных или нет
            if the_user.lower() == "y":
                clear_profit_sum = clear_profit
                revenue_sum = revenue
                Assets_at_the_last_reporting_date_sum = Assets_at_the_last_reporting_date
                own_capital_sum = own_capital
                return_on_equity_ratio = ROE(clear_profit_sum, revenue_sum, Assets_at_the_last_reporting_date_sum, own_capital_sum )
                if return_on_equity_ratio >= 20:
                    print(str(return_on_equity_ratio) +'%', 'Хороший показатель! В РФ значение коэффициента должно быть > или = 20%')
                else:
                    print(str(return_on_equity_ratio) +'%', 'Плохой показатель! В РФ значение коэффициента должно быть > или = 20%')
                break

            elif the_user.lower() == "n":
                clear_profit_sum += clear_profit
                revenue_sum += revenue
                Assets_at_the_last_reporting_date_sum += Assets_at_the_last_reporting_date
                own_capital_sum += own_capital
            else:
                print("Проверьте правильность ввода:\n(Y)-Да (N)-Нет\nПопробуйте еще раз!")
                break
    elif control_panel == 2:
        print("Вы вышли из программы")
        exit()


def ROE(clear_profit: float, revenue: float, Assets_at_the_last_reporting_date: float, own_capital: float)-> float:
    """Функция расчета коэфициента Рентабельности собственного капитала"""
    result = round((clear_profit / revenue) * (revenue / Assets_at_the_last_reporting_date) * (Assets_at_the_last_reporting_date / own_capital) * 100, 2)
    return result 


def Check_Data_One(control_panel: str) -> int:
    """Функция проверки и перевода данных c str во int"""
    try: 
        control_panel = int(control_panel)
        return control_panel
    except ValueError:
        print("Проверьте вводимые данные!")
        exit()


def Check_Data_Two(num: str) -> float:
    """Функция проверки и перевода данных c str во float"""
    try: 
        num = float(num)
        return num
    except ValueError:
        print("\nВы ввели не число!\nПопробуйте еще раз!")
        main(clear_profit_sum, revenue_sum, Assets_at_the_last_reporting_date_sum, own_capital_sum)


if __name__ == "__main__":
#while True:
    main(clear_profit_sum, revenue_sum, Assets_at_the_last_reporting_date_sum, own_capital_sum)








