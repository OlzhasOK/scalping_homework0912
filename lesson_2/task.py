import requests
from bs4 import BeautifulSoup

headers = {

    'accept': '*/*',

    'user-agent': 'Mozilla/5.0 (Linux; Android 7.1; Xperia V Build/NDE63X) AppleWebKit/600.3 (KHTML, like Gecko)  Chrome/55.0.2635.298 Mobile Safari/533.5',

}

for i in range(1, 4):
    print(f'Парсим {i} страницу')

    url = 'https://www.olx.kz/list/q-елки/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    cards = soup.find_all('div', class_='css-1sw7q4x')[:5] 
    schetchik = 0
    for card in cards:
        schetchik += 1
        card_url = card.a['href']
        url = f'https://www.olx.kz{card_url}'
        response = requests.get(url=url)
        soup = BeautifulSoup(response.text, 'html.parser')
        description = soup.find("div", class_="css-1t507yq er34gjf0")
        
        print(f'Описание номер {schetchik}:', description.text)


