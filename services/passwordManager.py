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
    with open(sys.path[0] + '\data\passwordManagerStorage.json') as test_file: #selects the file since they are in the same folder/dir
        test = json.load(test_file) #loads it into a python obj

    # This part of the code is what retrieves the password for the selected site
    sites = []
    sitesPasswords = []
    indexs = []
    i = 0
    for title in test["passwords"]: #opens the json from above
        if title != "": #Checks if the title is empty and if its not then continue (used to keep our placeholder in json functional and not appear on the menu)
            sites.insert(0, title["siteName"]) #inserts the title into the py object
            sitesPasswords.insert(0, title["password"])
            indexs.insert(0, i)
        i = i + 1

    return sites, sitesPasswords, indexs




# MAIN SERVICE
def passwordManager():
    mainOptions = ['Retrieve', 'Create', 'Delete Password', 'Generate Password']
    title = 'Please Choose an option.'
    option, index = pick(mainOptions, title)

    if option == 'Retrieve':
        sites, passwords, indexs = getAllPasswords()

        title2 = 'Please Choose an option'
        option2, index2 = pick(sites, title2) #Creates a menu

        i = 0
        for title in sites: #sorts thru all entries in the json ob
            if title == option2: #if title equals seleciton then
                copy2clip(passwords[i])
                print("Password has been copied to your clipboard! Program closing in 5 seconds")
                time.sleep(5) #wait 5 seconds before closing program
            else: i = i + 1


    elif option == 'Create':
        siteName = input('Input the name of the site: ')
        sitePass = input('Input your password: ')


        with open(sys.path[0] + '\data\passwordManagerStorage.json','r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data["passwords"].append({
                "siteName":siteName,
                "password": sitePass
            })
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)

        print("Password saved! Program Closing in 5 seconds")
        time.sleep(5)
    
    elif option == 'Delete Password':
        sites, passwords, indexs = getAllPasswords()

        title2 = 'Please Choose an option'
        option2, index2 = pick(sites, title2) #Creates a menu

        i = 0 #since the .pop index starts at -1 not 0
        for title in sites: #sorts thru all entries in the json ob
            if title == option2: #if title equals seleciton then
                with open(sys.path[0] + '\data\passwordManagerStorage.json') as file:
                    data = json.load(file)
                    data["passwords"].pop(indexs[i])

                with open(sys.path[0] + '\data\passwordManagerStorage.json','w') as file:
                    json.dump(data, file)
            i = i + 1

    elif option == 'Generate Password':
        genPassword = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation + string.ascii_letters) for i in range(20))
        copy2clip(genPassword)
        print("New Generated Password has been copied to your clipboard! Do note this password is not saved by this program to save it you will have to run the program again and choose the create option and enter the information! This program will close in 10 seconds.")
        time.sleep(10)

# The empty json obj in the json file is used as a placeholder as the last entry can not have a , at the end but any ones before it do this was a easy simple way to fix that