import json
from datetime import datetime
from os import path, system

import mysql.connector as c

from logout import logout

connection = c.connect(host='localhost', database='electricity_bill', user='root', password='') 
db = connection.cursor()

#Opening of config.json file
THIS_FOLDER = path.dirname(path.abspath(__file__))
my_file = path.join(THIS_FOLDER,'files','config_file', 'config.json')

with open(my_file, 'r') as c:
    params = json.load(c)["params"]

def bilGenHome(userid,logintime):
    '''This is the bill generation department homepage function'''

    mydate = datetime.now()
    system('cls') #Clear the screen

    #The bill generation welcome message
    billGenAdmin_message = open('files/messages/billGennotAdmin_message.txt','r').read()
    funcAdminTuple = ('01#02','00#01')

    print(billGenAdmin_message.format(params['company_name'],userid,logintime,datetime.now(),mydate.strftime("%B")))
    userinput = input()


    if userinput not in funcAdminTuple:
        system('cls') #Clear the screen
        bilGenHome(userid,logintime)
    
    else:
        if userinput=='01#02':
            pass
        elif userinput=='00#01':
            logout(userid)
