import hashlib
import json
import sys
import time
from datetime import datetime
from os import path, system

import mysql.connector as c

from admin import adminHome
from billGen import bilGenHome

connection = c.connect(host='localhost', database='electricity_bill', user='root', password='') 
db = connection.cursor()


#Opening of config.json file
THIS_FOLDER = path.dirname(path.abspath(__file__))
my_file = path.join(THIS_FOLDER,'files','config_file', 'config.json')

with open(my_file, 'r') as c:
    params = json.load(c)["params"]



#Welcome message
def welcome_message():
    '''The first welcome message'''
    system('cls') #Clear the screen
    #The welcome message
    welcome_message = open('files/messages/welcome_message.txt','r').read()
    print(welcome_message.format(params['company_name']))

    #Calling the login_deptno function
    login_deptno()





#Login system
############################################################################################################################################################################################################################################


######################################################################################################################

# The function 1 and 2 are related to each other
# The first function catches exception and the second function is for validation

# (1) Makes the user to get logged in into the correct deptno
def login_deptno(message=''):
    '''Makes the user to get logged in into the correct deptno'''
    while True:
        print(message)
        try:
            deptno_in = int(input('Please enter the department no.\n'))
            logincheck(deptno_in)
            break
        except ValueError:
            print()
            print('Please Enter a number not alphabets')


# (2) Checks the login (Validation)
def logincheck(deptno):
    '''This is a function to check if the user exists and gets him logged in'''

    #Department No dictionary
    db.execute('SELECT dept_no FROM dept')
    sqlquery = db.fetchall()
    deptno_dict = (i for i in sqlquery)

    #Check if the department no entered is correct
    newline='\n'
    if (deptno,) not in deptno_dict:
        login_deptno(f'{deptno} Department No is not valid {newline} Please enter a valid department no !')
    else:
        login_user(deptno)

######################################################################################################################


######################################################################################################################

# Similarly here the function 3 and 4 are realated to each other
# the 3rd function is used to logged the user anser in and 4th function is used for creatting a session and
# then give the user out the appropriate page 


#  (3) Make user logged in
def login_user(deptno):
    '''This is the login screen'''
    system('cls') #Clear the screen
    print()
    print('Now please enter your login credentials')
    print('---------------------------------------')
    userid=input('Please enter your USERID\n')
    print('---------------------------------------')
    password=input('Please enter your password\n')
    hashpass = hashlib.md5(password.encode())

    db.execute(f'SELECT * FROM user WHERE password="{hashpass.hexdigest()}" AND dept_no="{deptno}" AND useradmin_id="{userid}";')
    query = db.fetchall()

    if query==None or query==[]:
        print('The given credentials where wrong')
        print('Please wait for 2 sec!')
        time.sleep(2)
        welcome_message()
    else:
        login_user_in(userid,hashpass.hexdigest(),deptno)


#  (4) Checks the logged in user branch and gives out the appropriate page
def login_user_in(userid,hashpass,deptno,work=None):
    '''Checks the logged in user branch and gives out the appropriate page'''
    logintime = datetime.now()   #Creating session

    db.execute(f'SELECT branch FROM user WHERE useradmin_id="{userid}"')
    branch=db.fetchall()

    if work==None:
        db.execute(f'INSERT INTO login(userid,branch,session_in,dept_no) VALUES("{userid}","{branch[0][0]}","{logintime}","{deptno}")')
        connection.commit()
    else:
        db.execute(f'UPDATE login set session={datetime.now()} WHERE userid="{userid} AND session_out="0000%"')

    branchget = userid.split("#")
    print('Please wait you being redirected there! in 3 sec.....')
    time.sleep(3)

    #Validation
    branch = str(branchget[1])
    if branch=='ADMIN':
        adminHome(userid,logintime)
    elif branch=='BILL GENERATION':
        bilGenHome(userid,logintime)
    elif branch=='BILL DELIVERY':
        pass
######################################################################################################################

############################################################################################################################################################################################################################################
