

# **ELECTRICITY BILLING MANAGEMENT SYSTEM**

**DEVELOPED BY** : **Ayush Saha, Dhruva Shaw, Smyan Kotkar**
#
*THIS WAS OUR SCHOOL PROJECT*
#



# Content

| **Sl. No.** | **Topic** |
| --- | --- |
| **1** | **Modules Used**** (In-Built &amp; User created modules)** |
| **2** | **Objective, Scope &amp; Backbone of the Project** |
| **3** | **Table Structure Used** |
| **4** | **Working Description** |
| **6** | **Bibliography** |

# MODULES USED

## **Inbuilt modules**


- **sys** : The system module is used to close the interpreter programmatically using sys.exit()
- **mysql-connector** : This module is used to perform the backend operations with the MySQL database.
- **os** : This module is imported in the program clear the terminal screen programatically, get the current working directory and make the program Operating System independent.
- **json** : This module is used to import data from .json files to the program.
- **math** : From this module the ceil function is imported to roundoff the generated value for the electric bill.
- **smtplib** : This module is imported to send the electric bills to respective customer.
- **email** : This module is imported to work accordance with smtplib module and ease the template making of the emails.
- **datetime** : This module is imported to get the current time.
- **csv** : This module is imported to read and write the csv files.
- **hashlib** : This module is imported to hash the password using the md5 hash algorithm and return the hash in a hexadecimal number
- **time** : From this module sleep function is imported to suspend execution of the calling thread for the given number of seconds
- **cProfile** : This module is to provide a deterministic profiling of the python program
- **re** : From the regular expression module compile function imported and is used to compile a regular expression pattern into a regular expression object
- **pyinstaller** : This is used to convert the python file to exe file.


## **Custom (user made) Modules**

- **adminBillGen** : This contains function for the Admin Homepage.

- **clearscreen** : This contains the function for the clearscreen based on the operating system.

- **customerView** : This contains the function for the billing the view bill and this is accessible to customer only.

- **billEmail** : This contains the function for the emailing the bill to respective customer.

- **billGen** : This contains the function for to generate the bill for the corresponding month.

- **login** : This function to logged into the user in correct department.

- **logout** : This contains the function to logout the user.

## **Objective, Scope &amp; Backbone of the Project**

Our project entitled &quot; **Electricity Billing System**&quot; aim is to generate electricity bill with all the charges and penalty. Manual system that is employed is extremely laborious and quite inadequate. It only makes the process more difficult and hard. The aim of our project is to develop a system that is meant to partially computerize the work performed in the Electricity Board like generating monthly electricity bill, record of consuming unit of energy, store record of the customer and previous unpaid record. We used Python 3.8 as front end and MySql-marriaDB engine as back end for developing our project. Our project is independent of any OS and can run on any platform.

The overall project report is divided into further sub-parts which includes developing of the model system with scope for enhancement depending on the functionality of the organisation. The codes written were developed by the team jointly, tested with dummy data and found to be successful worth implementation with suitable modifications for further implementation.

**Backbone of the Project :**

This Project was completed using the methods which can be used in connecting MySQL and Python together. Python was chosen due to its simple structure, robustness and high capability in creating definitions. MySQL as a backend tool was chosen as a combination to give Python the meaning of flexibility and adaptability due it&#39;s simple table management system while primarily used for storing the data related to the billing system and customer details.

We as a team hope that the humble effort taken from our side would be able to create a significant change for the betterment of the lives of the people who would be using the system with adaptations as required.

**Table Structure**

| **Table Name** | **Customer** |                                                        
| --- | --- |
| **Field Name** | **Type** |
| id | integer |
| meterno | integer |
| consumerno | biginteger |
| consumername | varchar() |
| load\_con | varchar() |
| unit\_consumed | integer |
| month | varchar() |
| year | integer ||
| email | varchar() |
| address | text |
| amountgen | decimal |

##

| **Table** | **User** |
| --- | --- |
| **Field Name** | **Type** |
| id | int |
| username | varchar() |
| password | varchar() |
| branch | varchar() |
| dept\_no | int |
| useradmin\_id | varchar() |

##

| **Table Name** | **DEPT** |
| --- | --- |
| **Field Name** | **Type** |
| id | int |
| dept_no |int |
| deptname | text |

##

| **Table Name** | **Login** |
| --- | --- |
| **Field Name** | **Type** |
| id | int |
| userid | varchar() |
| branch | text |
| session\_in | datetime |
| session\_out | datetime |
| dept\_no | int |



# WORKING DESCRIPTION

- **FILES GENERATED**** :**

config.json, customer\_details.csv, employee\_details.csv, admin\_message.txt, billEmailnotAdmin\_message.txt, billGennotAdmin\_message.txt, create\_msg.txt, createdBill.txt, custdetails.txt, welcome\_message.txt

An exe file is generated for distribution.

- **DIRECTORY STRUCTURE**  **:**

The master folder contains a folder named &#39;files&#39;.

Then the files folder contains the following 5 folder.

config\_file&#39;, &#39;customerBillfolder&#39;, &#39;details&#39;, &#39;export&#39;, &#39;messages&#39;


The program has been designed with following modes of operation:

1. Admin
2. Bill Generation
3. Bill Delivery
4. Customer Bill View

Admin : It part has the privileges of a super user. It has the power to create, delete and edit, etc.

Bill Generation: This module has been designed to generate electricity bills based on the inputs of meter reading.

Bill Delivery: This module will email the bill to respective customers address and thus bring the concept of a reduce paper and reduce carbon footprint making the environment greener and sustainable.

Customer View Bill: This portal is only for use by the consumer to view the bill for the current month.

This is all in one program where electricity department can enter the data through the MySQL database, where a consumer can view its own bill just by using this program.

## Features:

It has an Admin Panel which the super user can access to enter the data of the consumer to database given by the electricity meter department in form of a csv file. It has a login system where the password are hashed using md5 hash algorithm then the hash are converted to the hexadecimal units. The super user can also add the details of a new operator or delete its details.

It also a configurable json file, and configure the contents of a program.

This program is also Operating System independent.

It also has a portal for the Bill Generation and Bill Delivery Department where the respective operator can generate the electricity bill with help of only one command and also deliver the bill to customers using their emails.

It has also portals for the customers where a consumer can enter its consumer no and get the bill details for the current month.

## Cons :

A constant Internet Connection is required.

The database of the consumer has to be constantly updated by the admin every month through csv files.

And in the customers or consumer portal in case of any emergency or help requiring situation one cannot contact any authority as would be required to resolve the problem in hand.

# Biblio graphy

- [https://www.codewithharry.com/](https://www.codewithharry.com/)
- [https://www.geeksforgeeks.org/](https://www.geeksforgeeks.org/)
- [https://www.python.org/doc/](https://www.python.org/doc/)
- [https://stackoverflow.com/](https://stackoverflow.com/)