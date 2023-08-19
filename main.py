import services.RedMScriptTemplateMaker as tm
import services.passwordManager as pm
import services.cfxWebScraper as cfxScraper
from pick import pick

mainOptions = ['Cfx Webscraper', 'Password Manager', 'RedM Script Template Maker']
title = 'Please Choose an option.'
option, index = pick(mainOptions, title)
if option == 'Cfx Webscraper':
    cfxScraper.cfxWebScraperMain()
elif option == 'RedM Script Template Maker':
    tm.createTemplate()
elif option == 'Password Manager':
    pm.passwordManager()