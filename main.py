import services.RedMScriptTemplateMaker as tm
import services.passwordManager as pm
import services.cfxWebScraper as cfxScraper
import services.epicGamesWebScraper as epicGamesScraper
from pick import pick

mainOptions = ['Cfx Webscraper', 'Epic Games Free Games Of The Week','Password Manager', 'RedM Script Template Maker']
title = 'Please Choose an option.'
option, index = pick(mainOptions, title)
if option == 'Cfx Webscraper':
    cfxScraper.cfxWebScraperMain()
elif option == 'RedM Script Template Maker':
    tm.createTemplate()
elif option == 'Password Manager':
    pm.passwordManager()
elif option == 'Epic Games Free Games Of The Week':
    epicGamesScraper.viewFreeGamesOfTheWeek()