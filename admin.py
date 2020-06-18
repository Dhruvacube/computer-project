import hashlib
import json
import sys
import time
from datetime import datetime
from os import path, system
from logout import logout
import csv
import os
import mysql.connector as c

connection = c.connect(host='localhost', database='electricity_bill', user='root', password='') 
db = connection.cursor()

#Opening of config.json file
THIS_FOLDER = path.dirname(path.abspath(__file__))
my_file = path.join(THIS_FOLDER,'files','config_file', 'config.json')

with open(my_file, 'r') as c:
    params = json.load(c)["params"]


#Admin
############################################################################################################################################################################################################################################


def adminHome(userid,logintime,userinput=0):
    #Here userinput is for the functioncode coming from the other function   
    '''This the admin homepage'''

    system('cls') #Clear the screen

    #The admin welcome message
    admin_message = open('files/messages/admin_message.txt','r').read()
    print(admin_message.format(params['company_name'],userid,logintime,datetime.now()))
    
    userinput=input()

    funcAdminTuple = ('01#01','05#02','06#03','04#01','00#01','02#01','07#44','03#01')

    if userinput not in funcAdminTuple:
        system('cls') #Clear the screen
        adminHome(userid,logintime)
    else:
        if userinput=='01#01':
            create_user(userid,logintime)
        elif userinput=='05#02':
            delete_user(userid,logintime)
        
        elif userinput=='06#03':
            dumpdata('customer',userid,logintime)
        elif userinput=='07#44':
            dumpdata('user',userid,logintime)

        elif userinput=='02#01':
            pass
        elif userinput=='03#01':
            pass
        elif userinput=='04#01':
            pass

        #For the Logout
        elif userinput=='00#01':
            logout(userid)


######################################################################################################################


######################################################################################################################

def create_user(userid23,logintime23):
    '''This function is used to create a user of the software'''
    system('cls') #Clear the screen
    db.execute('SELECT dept_no, deptname from dept')
    dept = db.fetchall()

    #Printing the department no
    print('     Department No       |             Department name')
    print('------------------------------------------------------------')
    for i,j in dept:
        print(f'      {i}                            {j}   ')
    print('Following are the department no')
    print()

    #Department No dictionary
    db.execute('SELECT dept_no FROM dept')
    sqlquery = db.fetchall()

    #Asking to enter the department no
    while True:
        try:
            deptno1 = int(input('Enter the department no\n'))

            if (deptno1,) in sqlquery:
                break
            else:
                print(f'{deptno1} Department No is not valid \n Please enter a valid department no !')
        except:
            print('Enter no not characters!')
    
    #Asking to enter the name
    name = input('Please enter the name\n')

    while True:
        #ENTERING THE PASSWORD
        password1 = input('Please enter a password\n')
        password2 = input('Please retype the password\n')
        if password1==password2:
            break
        else:
            system('cls')
            print('Enter again the two password dosen\'t match!')
    
    hashpass1 = hashlib.md5(password1.encode())
    db.execute(f'SELECT deptname FROM dept WHERE dept_no={deptno1}')
    #Getting the branch name
    branch = db.fetchall()[0][0]

    # generating the useradminid
    db.execute(f'select username from user where username="{name}"')
    occurence = len(db.fetchall())
    useradminid = f'{deptno1}{occurence+1}{name[:2]}#{branch}'

    #Inserting the data into database
    db.execute(f'INSERT INTO user VALUES(NULL,"{name}","{hashpass1.hexdigest()}","{branch}",{deptno1},"{useradminid}")')
    connection.commit()

    #The admin welcome message
    system('cls')
    created_message = open('files/messages/create_msg.txt','r').read()
    print(created_message.format(name,password1,branch,deptno1,useradminid))
    print()
    input('Press any key to continue')
    adminHome(userid23,logintime23)
######################################################################################################################


######################################################################################################################

def delete_user(userid,logintime):
    system('cls')
    #Department No dictionary
    db.execute('SELECT useradmin_id FROM user')
    sqlquery = db.fetchall()
    #Asking to enter the department no
    while True:
        UserAdminId = input('Enter the UserAdminId \n')

        if (UserAdminId,) in sqlquery:
            break
        else:
            print(f'{UserAdminId} UserAdminId is not valid \n Please enter a valid UserAdminId !')

    db.execute(f'DELETE FROM user WHERE useradmin_id="{UserAdminId}"')
    connection.commit()
    print('The user succesfully deleted')
    time.sleep(1)
    adminHome(userid,logintime)

######################################################################################################################


######################################################################################################################
def dumpdata(tablename,userid,logintime):
    QUERY = f'SELECT * FROM {tablename}'
    db.execute(QUERY)
    result=db.fetchall()

    if tablename=='user':
        filename = 'employee_details'
    else:
        filename = 'customer_details'

    c = csv.writer(open(f'files/details/{filename}.csv', 'a',newline=''))
    for x in result:
        c.writerow(x)
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print('The the data has been successfully dumped')
    print('The path of the file is:')
    print(os.path.join(BASE_DIR, 'files', 'details', f'{filename}.csv'))

    time.sleep(2)
    adminHome(userid,logintime)

######################################################################################################################