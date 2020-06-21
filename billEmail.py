import json
import os
from datetime import datetime
from os import path

import mysql.connector as c

from clearscreen import clear
from logout import logout

connection = c.connect(host='localhost', database='electricity_bill', user='root', password='') 
db = connection.cursor()

#Opening of config.json file
THIS_FOLDER = path.dirname(path.abspath(__file__))
my_file = path.join(THIS_FOLDER,'files','config_file', 'config.json')

with open(my_file, 'r') as c:
    params = json.load(c)["params"]

def bilEmailHome(userid,logintime):
    '''This is the bill generation department homepage function'''

    mydate = datetime.now()
    clear() #Clear the screen

    billGenAdmin_message = open('files/messages/billEmailnotAdmin_message.txt','r').read()
    funcAdminTuple = ('01#02','00#01')

    print(billGenAdmin_message.format(params['company_name'],userid,logintime,datetime.now(),mydate.strftime("%B")))
    userinput = input()


    if userinput not in funcAdminTuple:
        clear() #Clear the screen
        bilEmailHome(userid,logintime)
    
    else:
        if userinput=='01#02':
            pass
        elif userinput=='00#01':
            logout(userid)
