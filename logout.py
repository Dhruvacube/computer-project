import sys
import time
from datetime import datetime

import mysql.connector as c

from clearscreen import clear

connection = c.connect(host='localhost', database='electricity_bill', user='root', password='') 
db = connection.cursor()

#Logout function
def logout(userid):
    db.execute(f'UPDATE login SET session_out="{datetime.now()}" WHERE userid="{userid}" AND session_out="0000%"')
    connection.commit()

    clear()

    print(f'You have been logged out!!! {userid}')
    print('The window is closing the 2 sec')
    time.sleep(2)

    clear()
    sys.exit()
