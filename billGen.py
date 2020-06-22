import json
import time
from datetime import datetime
from math import ceil
from os import getcwd, path

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

def bilGenHome(userid,logintime):
    '''This is the bill generation department homepage function'''

    mydate = datetime.now()
    clear()

    #The bill generation welcome message
    billGenAdmin_message = open('files/messages/billGennotAdmin_message.txt','r').read()
    funcAdminTuple = ('01#02','00#01')

    print(billGenAdmin_message.format(params['company_name'],userid,logintime,datetime.now(),mydate.strftime("%B")))
    userinput = input()


    if userinput not in funcAdminTuple:
        clear()
        bilGenHome(userid,logintime)
    
    else:
        if userinput=='01#02':
            generateBill(userid,logintime)
        elif userinput=='00#01':
            logout(userid)



def generateBill(userid,logintime):
    mydate= datetime.now()
    month = mydate.strftime("%B")

    db.execute(f'SELECT unit_consumed,consumerno FROM customer WHERE month="{month}" AND amountgen=0.00000')
    consumerno = db.fetchall()

    #Now checking the database if the meter department has given the data
    if consumerno==[] or consumerno==None:
        print()
        print('No data for this month were provided by the Meter Department!')
        print('OR')
        print('The data was was generated already for this month!')
        print('Please contact your Meter Department!')
        time.sleep(2)
        bilGenHome(userid,logintime)
    
    db.execute(f'SELECT unit_consumed,consumerno FROM customer WHERE month="{month}"')
    consumerno = db.fetchall()
    
    #Getting the prevous reading and current reading
    counter=0
    for x,y in consumerno:
        db.execute(f'SELECT * From customer WHERE unit_consumed={x} AND consumerno={y}')
        custdetails = db.fetchall()[0]

        amountgen,rebate,aduj = Bill_Calc1(x)
        db.execute(f'UPDATE customer SET amountgen={amountgen} WHERE consumerno={y}')
        connection.commit()
        print(f'THE BILL FOR THE CONSUMER NO {y} IS GENERATED Rs.{amountgen}')
        print()

        counter+=1

        with open(path.join(getcwd(),'files','messages','createdBill.txt'),'r') as fileCreated:
            fileReadCreated = fileCreated.read()
            
            with open(path.join(getcwd(),'files','customerBillFolder',f'{x}{y}.txt'),'w+') as fileBillCreated:
                fileBillCreated.write(fileReadCreated.format(params['company_name'],custdetails[3],custdetails[1],custdetails[2],custdetails[4],custdetails[5],rebate,aduj,amountgen,custdetails[8],custdetails[9]))
            # UPDATE `customer` SET `amountgen` = '925.60001' WHERE `customer`.`id` = 1
    
    print(counter, " bills generated.")
    input('Press anything to continue')
    time.sleep(2)
    bilGenHome(userid,logintime)
    





def Bill_Calc1(unit):
    meter = 10               #Meter Rent
    MVCA = 60                # Metre Load charge
    fixedChrge = 100         #This is the fixed charge
    untstr = str(unit)[-1]   #This is the Adjustment Chrges

    if((unit>=1)and(unit<=50)):#between 1 - 50 units
        return (ceil(unit*4.89)+meter+MVCA+fixedChrge+int(untstr)-1,1,untstr) #At the end the price deducted is rebate
    
    elif((unit>50)and(unit<=150)):#between 50 - 150 units
    
        return (ceil((50*4.89)+(unit-50)*5.4)+meter+MVCA+fixedChrge+int(untstr)-1.4,1.4,untstr) #At the end the price deducted is rebate
    
    elif((unit>150)and(unit<=250)):#between 150 -  250 units
        return (ceil((50*4.89)+((150-50)*5.4)+(unit-150)*6.41)+meter+MVCA+fixedChrge+int(untstr)-1.5,1.5,untstr) #At the end the price deducted is rebate
    
    elif(unit>250):           #above 250 units
        return (ceil((50*4.89)+((150-50)*5.4)+((250-150)*6.41)+(unit-250)*7.16)+meter+MVCA+fixedChrge+int(untstr)-1.6 ,1.6,untstr) #At the end the price deducted is rebate
    else:
        return (0,0,0)
        #amount=0;