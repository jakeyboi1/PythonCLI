from pick import pick
import subprocess
import json
import sys
import time
import secrets
import string

#FUNCTIONS
def copy2clip(txt):
    cmd='echo ' + txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

def getAllPasswords():
    with open(sys.path[0] + '\data\passwordManagerStorage.json') as file:
        passwordStorageData = json.load(file)

    # This part of the code is what retrieves the password for the selected site
    allPasswords = {
        "sites": [],
        "sitePasswords": [],
        "indexs": []
    }
    i = 0
    for title in passwordStorageData["passwords"]:
        if title != "":
            allPasswords["sites"].insert(0, title["siteName"])
            allPasswords["sitePasswords"].insert(0, title["password"])
            allPasswords["indexs"].insert(0, i)
        i = i + 1

    return allPasswords

def retrievePassword():
    allPasswords = getAllPasswords()
    option2, index2 = pick(allPasswords["sites"], "Please Choose an option") #Creates a menu

    i = 0
    for title in allPasswords["sites"]: #sorts thru all entries in the json ob
        if title == option2: #if title equals seleciton then
            copy2clip(allPasswords["sitePasswords"][i])
            print("Password has been copied to your clipboard! Program closing in 5 seconds")
            time.sleep(5) #wait 5 seconds before closing program
        else: i = i + 1

def createPassword():
    siteName = input('Input the name of the site: ')
    sitePass = input('Input your password: ')

    with open(sys.path[0] + '\data\passwordManagerStorage.json','r+') as file:
        fileData = json.load(file)

        fileData["passwords"].append({ #Adding our data onto the existing data
            "siteName":siteName,
            "password": sitePass
        })
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json, and writing to the file.
        json.dump(fileData, file, indent = 4)

    print("Password saved! Program Closing in 5 seconds")
    time.sleep(5)

def deletePassword():
    allPasswords = getAllPasswords()
    option, index = pick(allPasswords["sites"], "Please Choose an option") #Creates a menu

    i = 0
    for title in allPasswords["sites"]:
        if title == option:
            with open(sys.path[0] + '\data\passwordManagerStorage.json') as file:
                data = json.load(file)
                data["passwords"].pop(allPasswords["indexs"][i])

            with open(sys.path[0] + '\data\passwordManagerStorage.json','w') as file:
                json.dump(data, file)
        i = i + 1

def generatePassword():
    genPassword = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation + string.ascii_letters) for i in range(20))
    copy2clip(genPassword)
    print("New Generated Password has been copied to your clipboard! Do note this password is not saved by this program to save it you will have to run the program again and choose the create option and enter the information! This program will close in 10 seconds.")
    time.sleep(10)

# MAIN SERVICE
def passwordManager():
    mainOptions = ['Retrieve', 'Create', 'Delete Password', 'Generate Password']
    option, index = pick(mainOptions, "Please Choose an option.")
    optionsArray = {
        "Retrieve": lambda: retrievePassword(),
        "Create": lambda: createPassword(),
        "Delete Password": lambda: deletePassword(),
        "Generate Password": lambda: generatePassword()
    }
    if option in optionsArray:
        optionsArray[option]()