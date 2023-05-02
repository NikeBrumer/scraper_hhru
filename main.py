import requests
from openpyxl import Workbook
from bs4 import BeautifulSoup
import os
from functions import returns_sheet

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
}
page = requests.get(
    'https://hh.ru/search/vacancy?text=python+тестовое&salary=&schedule=remote&area=1&ored_clusters=true',
    headers=header)
soup = BeautifulSoup(page.text, 'html.parser')
pages = soup.find(attrs={'data-qa': 'pager-next'})
work_book = Workbook()
work_sheet = work_book.active


while True:
    items = soup.find_all(class_='serp-item')
    if pages is None:
        returns_sheet(soup, work_sheet)
        break
    returns_sheet(soup, work_sheet)

    link = 'https://hh.ru' + pages.attrs['href']
    page = requests.get(f'{link}', headers=header)
    soup = BeautifulSoup(page.text, 'html.parser')
    pages = soup.find(attrs={'data-qa': 'pager-next'})


filename = 'Vacancies'
for i in range(2, 100):
    if os.path.exists(f'{filename}.xlsx'):
        filename = 'Vacancies'+str(i)
    else:
        break

work_book.save(f'{filename}.xlsx')
