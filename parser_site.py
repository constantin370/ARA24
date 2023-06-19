# 08.05.2023. Программа извлечения информации с сайта asko
# 1. Получить всю страничку!
# 2. Отсортировать полученные данные и вытащить нужные

 
import requests
from bs4 import BeautifulSoup


def main():
    """Главная Функция программы"""

    url = 'https://asko-bt.ru/asko-posudomoechnye-mashiny'
    html = Cheсk_Status(url)
    beautiful_response = beautiful_html(html)
    finding_link_machine(beautiful_response)
    finding_name_machine(beautiful_response)
    product_price(beautiful_response)
    recording_files(beautiful_response)
   

def Cheсk_Status(url: requests) -> requests:
    """Функция проверки сетевого статуса подключения"""

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return f'\nСоединение установленно: {response.status_code}\n'
        else:
            return f'\nОшибка соединения: {response.status_code}\n'   
    except requests.ConnectionError:
        print('Не удалось соедениться с сервером!')
    finally:
        return response.text


def beautiful_html(html: str) -> str:
    """Функция принимает HTML возвращает ссылку"""
    
    beautiful_response = BeautifulSoup(html, 'lxml')
    return beautiful_response


def finding_link_machine(beautiful_response: str) -> list:
    """Функция поиска и заполнения list_finding_link наденных ссылок 
Посудомоечных машины находящихся на странице"""

    list_finding_link = [ ]

    finding_link = beautiful_response.findAll("div", class_="col p-2 product")

    for dishwasher in finding_link: # type -> <class 'bs4.element.Tag'>
        list_finding_link.append("https://asko-bt.ru" + BeautifulSoup(str(dishwasher), 'lxml').
                    find("a", class_="stretched-link text-body card-link font-weight-bold").attrs['href'])
    print(list_finding_link)
    return list_finding_link


def finding_name_machine(beautiful_response: str) -> list:
    """Функция поиска наименования товара, а также очищения от лишних пробелов"""

    list_finding_name = [ ]
    list_clear_string = [ ]

    finding_name = beautiful_response.findAll("div", class_="card-body d-flex flex-column")
    
    for dishwasher in finding_name: # -> поиск наименования товара
        list_finding_name.append(BeautifulSoup(str(dishwasher), 'lxml').
                    find("a", class_="stretched-link text-body card-link font-weight-bold"))
        for iter in list_finding_name: # -> избовляемся от пробелов и заполнем список
            string = ' '.join(iter)
            clear_string = " ".join(string.split())
        list_clear_string.append(clear_string)
    print(list_clear_string)
    return list_clear_string


def product_price(beautiful_response: str):
    """Функция сбора цены товара"""

    list_finding_price = [ ]

    price = beautiful_response.findAll("div", class_="d-flex justify-content-between align-items-center mb-3 mt-4")

    for price_dishwasher in price:
        price_tag = BeautifulSoup(str(price_dishwasher), 'lxml').find("span", class_='lead text-danger font-weight-bold price text-nowrap').text
        list_finding_price.append(price_tag)
    return list_finding_price


def recording_files(beautiful_response: str) -> int:
    """Функция записи ссылок в блокнот txt"""

    finding_name_product = finding_name_machine(beautiful_response)
    finding_product = finding_link_machine(beautiful_response)
    price = product_price(beautiful_response)
 
    file_handler = open("C:/Users/Константин/Desktop/УРОКИ ПИТОН/parcer/write_3.txt", 'wt')
    dictionary = dict(zip(finding_name_product, price))
    file_recording = file_handler.write(str(dictionary))
    return file_recording


if __name__ == "__main__":
    main()
