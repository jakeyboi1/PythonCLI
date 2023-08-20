import requests
from bs4 import BeautifulSoup
import json

def viewFreeGamesOfTheWeek():
    r = requests.get('https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions', headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    soup = str(BeautifulSoup(r.content, 'html.parser'))
    split = soup.split("\n")
    loadedData = json.loads(r.content)
    if 'data' in loadedData:
        if 'Catalog' in loadedData['data']:
            if 'searchStore' in loadedData['data']['Catalog']:
                if 'elements' in loadedData['data']['Catalog']['searchStore']:
                    for index in loadedData['data']['Catalog']['searchStore']['elements']:
                        #print(index) use this to see the data
                        if 'price' in index:
                            if 'totalPrice' in index['price']:
                                if 'discountPrice' in index['price']['totalPrice']:
                                    if int(index['price']['totalPrice']['discountPrice']) == 0:
                                        if 'categories' in index:
                                            for k in index['categories']:
                                                if 'path' in k:
                                                    if k['path'] == 'freegames':
                                                        if index['title'] != 'PAYDAY 2':
                                                            print("Free Game: " + index['title'] )

    print('The games listed above are the free games of the week on Epic Games! Press "ENTER" at any time to close this program.')
    input()