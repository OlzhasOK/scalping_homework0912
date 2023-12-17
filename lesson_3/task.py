"""
Найти в API сайта технодома URL для получения смартфонов от Apple. 
Попробовать получить данные и сохранить в apple.json ТОЛЬКО те смартфоны у 
которых память 256Гб ИЗ ПЕРВЫХ 20 смартфонов.
"""
import json 
import requests
from bs4 import BeautifulSoup

apple_256gb = []

url = 'https://www.technodom.kz/catalog/smartfony-i-gadzhety/smartfony-i-telefony/smartfony/f/brands/apple'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

smartphones = soup.find_all('div', class_='ProductCardV_titleWrapper__a_HQC')

for smartphone in smartphones[:20]:
    memory = smartphone.find('p', class_='Typography ProductCardV_title__rFAYr ProductCardV_loading__TkTOe Typography__M')
    if memory and '256' in memory.text:
        apple_256gb.append({'phone': memory.text})

with open('./lesson_3/apple.json', 'w', encoding='utf-8') as file:
    json.dump(apple_256gb, file, ensure_ascii=False, indent=2)
