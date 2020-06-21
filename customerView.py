import mysql.connector as c
import datetime
from os import path
import json
import sys
import time
from clearscreen import clear

connection = c.connect(host='localhost', database='electricity_bill', user='root', password='') 
db = connection.cursor()

#Opening of config.json file
THIS_FOLDER = path.dirname(path.abspath(__file__))
my_file = path.join(THIS_FOLDER,'files','config_file', 'config.json')

with open(my_file, 'r') as c:
    params = json.load(c)["params"]


def consumerDetails():
    '''This function is the view page for the customers bill generation'''

    clear()

    db.execute('SELECT consumerno from customer')
    detailsconsumerno = db.fetchall()

    mydate = datetime.datetime.now()

    while True:
        try:
            consumerno = int(input('Please enter your consumer no.\n'))
        except ValueError:
            print()
            print("Please enter a valid consumer no")

        if (consumerno,) not in detailsconsumerno:
            print()
            print('The consumer no does not exists!! \nPlease enter a valid consumer no')
        else:
            break

    db.execute(f'SELECT * from customer where consumerno={consumerno} AND month="{mydate.strftime("%B")}"')
    custdetails = db.fetchall()[0]

    if custdetails[-1]==0:
        print('No bill is not generated for this month!')
    else:
        my_file1 = path.join(THIS_FOLDER,'files','messages', 'custdetails.txt')
        with open(my_file1, 'r') as c1:
            fileread = c1.read()
            print(fileread.format(params['company_name'],custdetails[3],custdetails[1],custdetails[2],custdetails[4],custdetails[5],custdetails[-1],custdetails[8],custdetails[9])) 
    
    print()
    print('Press anything the exit!!!')
    input()
    print(f"Thank you for using the {params['company_name']} ELECTRICITY CUSTOMER DEPARTMENT SERVICES")
    time.sleep(2)
    sys.exit()