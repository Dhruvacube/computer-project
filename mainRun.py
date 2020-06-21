
# Electricity bill management
# Computer Science project of class 12-Sc-1
# made by Dhruva, Ayush and Smyan
 
# import cProfile
# import re
# cProfile.run('re.compile("foo|bar")')
# input()


from datetime import datetime
from os import system
from login import welcome_message
from clearscreen import clear

import mysql.connector as c

connection = c.connect(host='localhost', database='electricity_bill', user='root', password='') 
db = connection.cursor()

#__main__
#Checks if the user is already logged in 
clear()

db.execute(f'UPDATE login SET session_out="{datetime.now()}" WHERE session_out="0000%"')
connection.commit()
welcome_message()