from bs4 import BeautifulSoup
import requests
import datetime


def get_exchange_rates(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    currency_names = soup.select('a[href^="/kursy-valyut/natsbank-rb/"]')
    values = soup.select('td[class=align-bottom]')
    correct_values = [val.contents[0].strip() for val in values]

    with open('exchange_rates.txt', 'a') as file:
        file.write(f'\n{datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")}\n{"=" * 20}\n')
        for name, value in zip(currency_names, correct_values):
            file.write(f'{name.text} {value}\n')


def main():
    get_exchange_rates(resource)


if __name__ == '__main__':
    resource = 'https://select.by/kurs/'
    main()
