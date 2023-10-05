import requests
import json

def viewFreeGamesOfTheWeek():
    r = requests.get('https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions', headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    loadedData = json.loads(r.content)
    if loadedData["data"]["Catalog"]["searchStore"]["elements"]:
        for index in loadedData['data']['Catalog']['searchStore']['elements']:
            if index["price"]["totalPrice"]["discountPrice"] == 0 and index["title"] != "PAYDAY 2":
                print("Free Game: " + index['title'] )

    print('The games listed above are the free games of the week on Epic Games! Press "ENTER" at any time to close this program.')
    input()