import json
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from os import path, getcwd
import time

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
            sendmailtocustomers(userid,logintime)
        elif userinput=='00#01':
            logout(userid)

def sendmailtocustomers(userid,logintime):
    port, smtp_server = 465, 'smtp.gmail.com'
    login, password = params['email'], params['password_email']

    mydate = datetime.now()

    db.execute(f'SELECT email,consumername, consumerno FROM customer WHERE month="{mydate.strftime("%B")}"')
    data = db.fetchall()

    message = MIMEMultipart()
    message["from"] = login

    error,emailno = 0,0
    for x,y,z in data:
        message["subject"] = f"Your electricity bill has been generated for the month {mydate.strftime('%B')}  ({y})"
        
        db.execute(f'SELECT unit_consumed FROM customer WHERE month="{mydate.strftime("%B")}" AND consumerno="{z}"')
        unitsConsumed = db.fetchall()[0][0]
        try:
            with open(path.join(getcwd(),'files','customerBillFolder',f'{unitsConsumed}{z}.txt'),'r') as bill:
                body = bill.read()
                
                with smtplib.SMTP(smtp_server, port) as server:
                    server.login(login, password)
                    server.sendmail(message["from"], x, body)
                    print(f"Email (BILL) sent to {y}")
                    print()
                    emailno+=1
        except:
            print('There was some error!')
            print()
            error+=1
    
    print(emailno, " Email sent!")
    print("With ",error," errors!")
    print()
    print("Now please wait for two seconds!")
    time.sleep(2)
    bilEmailHome(userid,logintime)


        

