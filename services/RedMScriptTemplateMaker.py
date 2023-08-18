import os

def createTemplate():
    print('Input the name of your script')
    input1 = input()

    print("input the directory the script should be located at")
    input2 = input()



    if input1 != '' and input2!= '': #making sure that the inputs are not empty
        #Main Dir Creation
        path = os.path.join(input2, input1)
        os.mkdir(path)

        #Client Creation
        cpath = os.path.join(path, 'client')
        os.mkdir(cpath)
        with open(cpath + '/functions.lua', 'w') as fp2:
            fp2.write('VORPcore = {}\nTriggerEvent("getCore", function(core)\n  VORPcore = core\nend)\nVORPutils = {}\nTriggerEvent("getUtils", function(utils)\n  VORPutils = utils\nend)')
        with open(cpath + '/client.lua', 'w') as fp4:
            fp4.write('--Insert Your Main Client Side Code Here')

        #Server Creation
        spath = os.path.join(path, 'server')
        os.mkdir(spath)
        with open(spath + '/server.lua', 'w') as fp3:
            fp3.write('VORPcore = {}\nTriggerEvent("getCore", function(core)\n  VORPcore = core\nend)\nVORPInv = {}\nVORPInv = exports.vorp_inventory:vorp_inventoryApi()')

        #Config Creation
        with open(path + '/config.lua', 'w') as fp5:
            fp5.write("Config = {}\n\nConfig.Setup = {\n    --Insert your config options here\n}")

        #ReadMe Creation
        with open(path + '/README.md', 'w') as fp6:
            fp6.write("Insert your readme info here")

        #FxManifest Creation
        with open(path + '/fxmanifest.lua', 'w') as fp:
            fp.write('fx_version "adamant"\ngames {"rdr3"}\nrdr3_warning "I acknowledge that this is a prerelease build of RedM, and I am aware my resources *will* become incompatible once RedM ships."\n\nlua54 "yes"\n\nshared_scripts {\n  "config.lua"\n}\n\nserver_scripts {\n  "/server/server.lua"\n}\n\nclient_scripts {\n  "/client/functions.lua",\n  "/client/client.lua"\n}')