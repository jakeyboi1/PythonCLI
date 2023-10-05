#Credit to Bytesizd for bcc-cfx-parser which was used as a guide basically
import requests
import time
import sys
import json
import re
from pick import pick
from bs4 import BeautifulSoup

def cfxWebScraperMain():
    mainOptions = ['Update Stored Cache', 'Display Total Player Count', 'Check How Many Servers Use A Resource']
    title = 'Please Choose an option.'
    option, index = pick(mainOptions, title)
    if option == 'Update Stored Cache':
        initReq = requests.get('https://servers-frontend.fivem.net/api/servers/stream', headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}) #headers is needed otherwise status_code will be 403 aka failed/forbidden 200 is success
        soup = str(BeautifulSoup(initReq.content, 'html.parser')) #If this is not the .split will not be usable and the parsed will always be zero. Likely because normally its all on one line of code and this makes it look like normal html so \n aka new line can detect the lines etc

        print("Server List Obtained!")
        parsed = []
        output = []
        splited = soup.split("\n")
        print("Parsing Server List...")
        for index in range(len(splited)):
            element = splited[index]
            l = re.match(r'\u0006[a-z0-9][a-z0-9][a-z0-9][a-z0-9][a-z0-9][a-z0-9]', element) #likely looks for this string in the element
            if l:
                cleaned = l.group(0).replace("\u0006", "")
                if cleaned != "locale":
                    parsed.append(cleaned) #adds it to the cleaned obj


        print('This many servers have been found: ' + str(len(parsed)))
        print("Sorting through the servers.")

        for index in range(len(parsed)):
            id = parsed[index]
            print("Retrieving ID: " + str(id) + " Processed: " + str(1 + index) + "/" + str(len(parsed))) #1 + index is done so you never see zero as it makes no sense in the progress part(Lua is best for indexing starting at 0 makes no sense anyone who says otherwise is wrong 1 sheep 2 sheep not 0 sheep 1 sheep)
            repeat = False
            recInfo = False
            recInfoLoaded = False
            rateLimitPrint = False #To only print being rate limited once
            while not repeat: #Checks if the key response exists (if the rate limiter is triggered the value of il will be {"response":"Too many requests."} which will break the code and also provide inaccurate data, so this is error handling basically) This whole while loop is done just because of rate limiting :( because of this, it is not viable to run this every time you want to check the data, it will have to be cached, then you will have to call the data from the cache, and the cache will need to be updated once a day ish, just not feasible to call this everytime just running through 100 ids takes about 3 minutes
                getServerReq = requests.get("https://servers-frontend.fivem.net/api/servers/single/"+str(id), headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
                recInfo = getServerReq.content #Do not use beautifal soup here as it will break the ["Data"] below
                recInfoLoaded = json.loads(recInfo)
                if 'response' in recInfoLoaded:
                    if recInfoLoaded["response"] == 'Too many requests.':
                        if not rateLimitPrint:
                            print("Currently being rate limited")
                            rateLimitPrint = True
                        time.sleep(2)
                        getServerFailsafeReq = requests.get("https://servers-frontend.fivem.net/api/servers/single/"+str(id), headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
                        recInfo = getServerFailsafeReq.content
                        recInfoLoaded = json.loads(recInfo)
                    else: # This should never be triggered but incase it ever does get triggered we dont want it to break anything by not resetting repeat
                        repeat = True
                else:
                    repeat = True
                    rateLimitPrint = False
                    print("Did not get rate limited.")
                    time.sleep(.3) #Best wait amount to balance not being rate limited but keep decent speed as with .3 it rarely gets rate limited (If no rate limits occur the process with the current amount of servers (24190) will take around 2 hours to complete and update the cache)
                    output.append(recInfo)


        print("Begin Analyzing data...")
        fivem = {
            'players': 0,
            'resources': {}
        }
        redm = {
            'players': 0,
            'resources': {}
        }
        data = output
        for p in range(len(data)):
            serverLoaded = json.loads(data[p])
            if 'Data' in serverLoaded: #Makes sure the Data key exists in the json file prevents errors and ensure accurate data
                server = serverLoaded["Data"]
                if server['vars']['gamename'] == 'gta5':
                    fivem['players'] += len(server['players'])
                    for ps in range(len(server['resources'])):
                        resource = server['resources'][ps]
                        if resource in fivem['resources']:
                            fivem['resources'][resource] += 1
                        else:
                            fivem['resources'][resource] = 1
                elif server['vars']['gamename'] == 'rdr3':
                    redm['players'] += len(server['players'])
                    for ps in range(len(server['resources'])):
                        resource = server['resources'][ps]
                        if resource in redm['resources']:
                            redm['resources'][resource] += 1
                        else:
                            redm['resources'][resource] = 0

        gtaPath = sys.path[0] + '\data\\fivem_analyzed_data.json'
        with open(str(gtaPath), 'w') as file:
            file.write(json.dumps(fivem))

        print(f"FiveM analysis is done and successfully written to ({gtaPath})!")
    
        rdmPath = sys.path[0] + '\data\\redm_analyzed_data.json'
        with open(str(rdmPath), 'w') as file:
            file.write(json.dumps(redm))

        print(f"RedM analysis is done and successfully written to ({rdmPath})!")
        print("Cache Updated Successfully, program closing in 5 seconds!")
        time.sleep(5)
    elif option == 'Display Total Player Count':
        mainOptions2 = ['RedM', 'FiveM']
        title2 = 'Choose Game You want to check.'
        option2, index2 = pick(mainOptions2, title2)
        if option2 == 'RedM':
            rdmPath = sys.path[0] + '\data\\redm_analyzed_data.json'
            f = open(rdmPath)
            data = json.load(f)
            print('Total Players Playing: ' + str(data["players"]))
            print("Program will close in 10 seconds.")
            time.sleep(10)
        elif option2 == 'FiveM':
            fivemPath = sys.path[0] + '\data\\fivem_analyzed_data.json'
            f = open(fivemPath)
            data = json.load(f)
            print('Total Players Playing: ' + str(data["players"]))
            print("Program will close in 10 seconds.")
            time.sleep(10)
    elif option == 'Check How Many Servers Use A Resource':
        mainOptions2 = ['RedM', 'FiveM']
        title2 = 'Choose Game You want to check for the resource.'
        option2, index2 = pick(mainOptions2, title2)
        if option2 == 'RedM':
            print("Input the name of the resource, captilization and spelling is crucial!")
            rss = input()
            rdmPath = sys.path[0] + '\data\\redm_analyzed_data.json'
            f = open(rdmPath)
            data = json.load(f)
            if str(rss) in data["resources"]:
                print(str(data["resources"][str(rss)]))
            else:
                print('Resource Not Found Closing in 5 seconds')
                time.sleep(5)
        elif option2 == 'FiveM':
            print("Input the name of the resource, captilization and spelling is crucial!")
            rss = input()
            fivemPath = sys.path[0] + '\data\\fivem_analyzed_data.json'
            f = open(fivemPath)
            data = json.load(f)
            if str(rss) in data["resources"]:
                print(str(data["resources"][str(rss)]))
            else:
                print('Resource Not Found Closing in 5 seconds')
                time.sleep(5)