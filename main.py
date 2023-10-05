import services.RedMScriptTemplateMaker as tm
import services.passwordManager as pm
import services.cfxWebScraper as cfxScraper
import services.epicGamesWebScraper as epicGamesScraper
import services.fileEncryptor as fileEncryptor
import requests
from pick import pick

##Version Checking
currentVersion = "1.0.1"
versionReq = requests.get("https://api.github.com/repos/jakeyboi1/PythonCLI/releases/latest")
if currentVersion != versionReq.json()["tag_name"]:
    print("OUTDATED!")
    print(f"A new version of this tool has been released, version {versionReq.json()['tag_name']} go download it at\nhttps://github.com/jakeyboi1/PythonCLI/releases/latest\nPress enter to launch the program without updating.")
    input()

#Main program
mainOptions = ['Cfx Webscraper', 'Epic Games Free Games Of The Week','Password Manager', 'RedM Script Template Maker', 'File Encryptor']
option, index = pick(mainOptions, "Please Choose an option.")
optionsArray = {
    "Cfx Webscraper": lambda: cfxScraper.cfxWebScraperMain(),
    "RedM Script Template Maker": lambda: tm.createTemplate(),
    "Password Manager": lambda: pm.passwordManager(),
    "Epic Games Free Games Of The Week": lambda: epicGamesScraper.viewFreeGamesOfTheWeek(),
    "File Encryptor": lambda: fileEncryptor.fileEncryptorMainMenu() #lambda in python is used for "anonymous" functions(only useful for inline functions can not span multiple lines)
}
if option in optionsArray:
    optionsArray[option]()