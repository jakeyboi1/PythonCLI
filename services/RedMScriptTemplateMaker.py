import os

def createDir(dirPath, dirName):
    path = os.path.join(dirPath, dirName)
    os.mkdir(path)
    return path

def createAndWriteToFile(filePath, contentToWrite):
    with open(filePath, 'w') as file:
        file.write(contentToWrite)

def createTemplate():
    print('Input the name of your script')
    scriptName = input()

    print("input the directory the script should be located at")
    scriptDirectory = input()

    if scriptName != '' and scriptDirectory != '': #making sure that the inputs are not empty
        #Main Dir Creation
        mainScriptPath = createDir(scriptDirectory, scriptName)

        #Client Dir Creatin
        clientPath = createDir(mainScriptPath, 'client')

        #Client Files Creation
        createAndWriteToFile(clientPath + "/functions.lua", 'VORPcore = {}\nTriggerEvent("getCore", function(core)\n  VORPcore = core\nend)\nVORPutils = {}\nTriggerEvent("getUtils", function(utils)\n  VORPutils = utils\nend)')
        createAndWriteToFile(clientPath + "/client.lua", "--Insert Your Main Client Side Code Here")

        #Server Creation
        serverPath = createDir(mainScriptPath, 'server')
        createAndWriteToFile(serverPath + "/server.lua", 'VORPcore = {}\nTriggerEvent("getCore", function(core)\n  VORPcore = core\nend)\nVORPInv = {}\nVORPInv = exports.vorp_inventory:vorp_inventoryApi()')

        #Config Creation
        createAndWriteToFile(mainScriptPath + '/config.lua', "Config = {}\n\nConfig.Setup = {\n    --Insert your config options here\n}")

        #ReadMe Creation
        createAndWriteToFile(mainScriptPath + '/README.md', 'Insert your readme info here')

        #FxManifest Creation
        createAndWriteToFile(mainScriptPath + '/fxmanifest.lua', 'fx_version "adamant"\ngames {"rdr3"}\nrdr3_warning "I acknowledge that this is a prerelease build of RedM, and I am aware my resources *will* become incompatible once RedM ships."\n\nlua54 "yes"\n\nshared_scripts {\n  "config.lua"\n}\n\nserver_scripts {\n  "/server/server.lua"\n}\n\nclient_scripts {\n  "/client/functions.lua",\n  "/client/client.lua"\n}')