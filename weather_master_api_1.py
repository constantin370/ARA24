#(А) - 30.06.2023 Программа показа Погоды
#(B) - Производим импорт всех необходимых модулей...
from api_weather import WEATHER_TOKEN
import requests
import json
from tkinter import *
import time
import datetime


def main():
    \
    """Главное меню программы (Прогноз Погоды)"""
#(1) - Создание главного окна программы при помощи кроссплатформенной библиотеки tkinter
# для разработки графического интерфейса на языке Python... 
    display = Tk()
    display.geometry("500x400")
    display.title("Прогноз Погоды")
    display["bg"] = "violet"
    

    def input_and_image_control_function():
        \
        """Главная Функция управления программой"""
#(2) - данная функция принимает вводимые данные пользователя через графический интерфейс...
#(3) - здесь происходит вызов основного функционала программы...
        moving_the_input_city_name = input_window.get()
        display.title(f'{moving_the_input_city_name.upper()}, Погода')

        if moving_the_input_city_name:

            WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?q=' + moving_the_input_city_name + '&appid='+ WEATHER_TOKEN
            response_weather = requests.get(WEATHER_URL)
            response_connect = Check_Status(moving_the_input_city_name, response_weather)

            if response_connect == 200:

                weather = take_my_weather(response_weather)
                translating = weather_translating(response_weather)
                time_processing_function(weather, translating, response_weather)
                take_my_variable_time = time_processing_function(weather, translating, response_weather)
                city_display(display, moving_the_input_city_name)
                temp_display(display, weather["temperature"])
                temp_feels_display(display, weather["temperature_feels"])
                weather_condition_display(display, translating)
                time_display(display, take_my_variable_time["local_time"])
            else:
                mistake_display(display, response_connect, moving_the_input_city_name)
        else:
            print("ERROR: Empty String")
 #(4) - добавление основных эллементов управления интерфесом программы на галвное окно...  
    master_label =Label(text="Название города", font=("Times New Roman", 20), foreground="black", background="Pink", height=2, width=20)
    input_window = Entry(display, font=("Times New Roman", 25), width=20, foreground="Navy blue", background="white")

    master_label.pack(side="top")
    input_window.pack(side="top")

    input_button = Button(display, font=("Times New Roman", 20), 
height=1, width=15, foreground="black", background="Pink", text="УЗНАТЬ ПОГОДУ", command=input_and_image_control_function, pady=10)
    
    input_button.pack(side="bottom", pady=10)

    display.mainloop()


def Check_Status(value: str, response_weather: requests) -> int:
    \
    """Функция проверки сетевого статуса"""

    try:
        if response_weather.status_code == 200:
            return response_weather.status_code
        else: 
            "city not found" in response_weather.text
            time.sleep(1)
            print(f'''\nОшибка соединения: {response_weather.status_code} 
Город {value} не существует!\nПопробуйте еще раз\n''')
            time.sleep(2)
            #return main() 
    except requests.ConnectionError:
        time.sleep(1)
        print(f'\nОшибка соединения: {response_weather.status_code}\n')
        time.sleep(2)
        return main()
    except requests.ReadTimeout:
        return exit()
    finally:
        return response_weather.status_code 


def take_my_weather(response_weather: requests) -> dict:
    \
    """Функция составления свотки погоды по введеному городу"""

    json_file_сreate = json.loads(response_weather.text)
    dict_weather = {}

    temperature = (json_file_сreate['main']['temp'] - 273.15)
    temperature_feels = (json_file_сreate['main']['feels_like'] - 273.15)
    temperature = int(temperature)
    temperature_feels = int(temperature_feels)
    city = json_file_сreate['name']

    dict_weather = {
        "temperature" : temperature,
        "temperature_feels" : temperature_feels,
        "city" : city
    }
    return dict_weather 


def weather_translating(response_weather: requests) -> str:
    \
    """Функция переводчик с англ -> рус"""

    json_file_сreate = json.loads(response_weather.text)

    for elem in json_file_сreate["weather"]:
        weather_state = elem['main']
    if weather_state == 'Clear':
        weather_state = 'Погода Ясная'
    elif weather_state == 'Rain':
        weather_state = 'Дождь'
    elif weather_state == 'Clouds':
        weather_state = 'Облачно'
    elif weather_state == 'Mist':
        weather_state = 'Туман'
    elif weather_state == 'Haze':
        weather_state = 'Лёгкий Туман'
    elif weather_state == "Thunderstorm":
        weather_state = 'Гроза'
    elif weather_state == "Snow":
        weather_state = 'Снег'
    return str(weather_state)


def time_processing_function(weather: dict, translating: str, response_weather: requests) -> dict:
    \
    """Функция обработки временных показателей"""

    json_file_сreate = json.loads(response_weather.text)

    sunrise_time = datetime.datetime.utcfromtimestamp(json_file_сreate['sys']['sunrise'] + 
json_file_сreate['timezone'])
    sunset_time = datetime.datetime.utcfromtimestamp(json_file_сreate['sys']['sunset'] + 
json_file_сreate['timezone'])
    local_time = datetime.datetime.now().strftime("%H:%M:%S")

    dictionary = {
        "local_time": local_time
    }
    return dictionary


def city_display(display, things):
    \
    """Функция отображения наименования города"""

    indicator = Label(display, text=f'{things}')
    indicator.config(font=("Consolas", 16))
    indicator.pack(side="top")
    return indicator


def temp_display(display, things):
    \
    """Функция отображения фактической температуры"""

    indicator = Label(display, text=f'Температура: {things}°C')
    indicator.config(font=("Consolas", 16))
    indicator.pack(side="top")
    return indicator


def temp_feels_display(display, things):
    \
    """Функция отображения ощущаемой температуры"""

    indicator = Label(display, text=f'Ощущается: {things}°C')
    indicator.config(font=("Consolas", 16))
    indicator.pack(side="top")
    return indicator


def weather_condition_display(display, things):
    \
    """Функция отображения состояния погоды"""

    indicator = Label(display, text=f'{things}')
    indicator.config(font=("Consolas", 16))
    indicator.pack(side="top")
    return indicator


def time_display(display, things):
    \
    """Функция отображения времения по текущему местоположению"""

    indicator = Label(display, text=f'Время Вашего местоположения:\n{things}')
    indicator.config(font=("Consolas", 16))
    indicator.pack(side="top")
    return indicator 


def mistake_display(display, things_1, things_2):
    \
    """Функция выовда информации об ошибке на главный экран"""

    mistake = Label(display, text=f'''\nОшибка соединения: {things_1}\n
(1). Возможно города: {things_2.upper()} не существует!\n
(2). В названии города допущена ошибка\n
(3). Возникли проблемы с интернет соединением\n
Попробуйте еще раз''')
    mistake.config(font=("Arial", 12 ))
    mistake.pack(side="top")


if __name__ == "__main__":
    main()