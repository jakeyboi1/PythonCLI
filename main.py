import services.RedMScriptTemplateMaker as tm
import services.passwordManager as pm
import services.cfxWebScraper as cfxScraper
import services.epicGamesWebScraper as epicGamesScraper
import services.fileEncryptor as fileEncryptor
from pick import pick

mainOptions = ['Cfx Webscraper', 'Epic Games Free Games Of The Week','Password Manager', 'RedM Script Template Maker', 'File Encryptor']
title = 'Please Choose an option.'
option, index = pick(mainOptions, title)
optionsArray = {
    "Cfx Webscraper": lambda: cfxScraper.cfxWebScraperMain(),
    "RedM Script Template Maker": lambda: tm.createTemplate(),
    "Password Manager": lambda: pm.passwordManager(),
    "Epic Games Free Games Of The Week": lambda: epicGamesScraper.viewFreeGamesOfTheWeek(),
    "File Encryptor": lambda: fileEncryptor.fileEncryptorMainMenu() #lambda in python is used for "anonymous" functions(only useful for inline functions can not span multiple lines)
}

if option in optionsArray:
    optionsArray[option]()