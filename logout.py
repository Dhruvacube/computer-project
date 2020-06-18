import sys
import time
from datetime import datetime
from os import system

import mysql.connector as c

connection = c.connect(host='localhost', database='electricity_bill', user='root', password='') 
db = connection.cursor()

#Logout function
def logout(userid):
    db.execute(f'UPDATE login SET session_out="{datetime.now()}" WHERE userid="{userid}" AND session_out="0000%"')
    connection.commit()

    system('cls') #Clear the screen
    print(f'You have been logged out!!! {userid}')
    print('The window is closing the 2 sec')
    time.sleep(2)
    system('cls') #Clear the screen
    sys.exit()