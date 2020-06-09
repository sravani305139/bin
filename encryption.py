import base64
import LogGenModule
import csv
import getpass
import datetime
import json


def encrypt(msg):
    try :
        key = "AutoFactCIS1569"
        encryped = []
        encoded = base64.b64encode((msg).encode('utf-8'))
        for i, c in enumerate(str(encoded.decode('ascii'))):
            key_c = ord(key[i % len(key)])
            msg_c = ord(c)
            encryped.append(chr((msg_c + key_c) % 127))
        return ''.join(encryped)
    except Exception as e:
        LogGenModule.Exception("error occured while encrypting the data")


def updateJsonFile(user,password,instance):
    jsonFile = open("./json_files/snow_login.json", "r") # Open the JSON file for reading
    data = json.load(jsonFile) # Read the JSON into the buffer
    jsonFile.close() # Close the JSON file

    ## Working with buffered content
    #tmp = data["location"] 
    data['Instance Details'][0]['user'] = user
    data['Instance Details'][0]['password'] = password
    data['Instance Details'][0]['instance'] = instance
    ## Save our changes to JSON file
    jsonFile = open("./json_files/snow_login.json", "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()

if __name__=='__main__':
    try:
        #logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s',datefmt='%a, %d-%b-%Y %H:%M:%S -', filename = datetime.datetime.now().strftime('../Logs/log_%d_%m_%Y.log'))
        instance = input("Enter the Servicenow Instance ")
        ins_user = input("Enter the Servicenow user ")
        ins_password = getpass.getpass("Enter the Servicenow password ")
        
        user = encrypt(ins_user)
        password= encrypt(ins_password)
        updateJsonFile(user,password,instance)
        print("Servicenow user : "+encrypt(ins_user))
        print("Servicenow password : "+encrypt(ins_password))
        
    except Exception as e:
        LogGenModule.Exception("error occured")