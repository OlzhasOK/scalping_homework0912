import json 
import requests
from bs4 import BeautifulSoup

url = 'https://tengrinews.kz/news/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')

quotes = soup.find_all('span', class_ ='tn-hidden')

data = []

for i in range(len(quotes)):
    new_quote = {}
    new_quote['quote'] = quotes[i].text
    data.append(new_quote)

with open('./quotes.json', 'w', encoding='utf-8') as fp:
    json.dump(data, fp, ensure_ascii=False, indent=4)