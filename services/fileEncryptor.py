from cryptography.fernet import Fernet
from pick import pick

def fileEncryptorMainMenu():
    mainOptions = ["Encrypt File", "Decrypt File"]  
    title = "Please Choose an option."
    option, index = pick(mainOptions, title)
    optionsArray = {
        "Encrypt File": lambda: fileEncryptor(),
        "Decrypt File": lambda: fileDecryptor()
    }
    if option in optionsArray:
        optionsArray[option]()

def fileEncryptor():
    #Getting location of file to encrypt
    print("Input the directory of the file you want to encrypt")
    fileDir = input()

    #Generating our encryption key
    encryptionKey = Fernet.generate_key()
    loadedEncryptionKey = Fernet(encryptionKey) #Note this is only used to actually encrypt the file, the key itself is the encryptionKey this is essentially loading our key into fernet

    #Encryption our file by reading the data in the file encrypting it then writing the new data to the file
    fileContents = open(fileDir, 'rb').read()
    open(fileDir, 'wb').write(loadedEncryptionKey.encrypt(fileContents))

    # Finishing up
    print('File encrypted Success your key is displayed below! Store this safely or this file will be permanetly encrypted. Press enter to close this program\n\n')
    print(encryptionKey.decode('utf-8')) #Prints the decrypted version of the key if u dont decrypt it will have b'' around the key and cause a error
    input()

def fileDecryptor():
    # Gets the location of the file to decrypt
    print('Input the directory of the file you wish to decrypt(Note this script can only decrypt files it encrypted!)')
    fileDir = input()

    # Gets the encryption key for this file
    print('Input the encryption key for this file')
    encryptionKey = Fernet(input())

    # Decrypts the file
    encryptedFilesContent = open(fileDir, 'rb').read()
    open(fileDir, 'wb').write(encryptionKey.decrypt(encryptedFilesContent))

    #Finishing up
    print("Your file has successfully been decrypted, press enter to close this program")
    input()