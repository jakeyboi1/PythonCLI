import services.RedMScriptTemplateMaker as tm
import services.passwordManager as pm
from pick import pick

mainOptions = ['RedM Script Template Maker', 'Password Manager']
title = 'Please Choose an option.'
option, index = pick(mainOptions, title)
if option == 'RedM Script Template Maker':
    tm.createTemplate()
elif option == 'Password Manager':
    pm.passwordManager()