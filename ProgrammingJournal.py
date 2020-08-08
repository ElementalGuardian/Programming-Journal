#!/usr/bin/env python3
import sys
import logging
import datetime

x = datetime.datetime.now()

lg = 'ProgrammingJournalLogs.log'

LOG_FILENAME = lg
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

username = "User"
password = "Password"

def Append():
    appendFile = open('ProgrammingJournal.txt','a')
    print("Hello " + username + ",What would you like to tell me today?: ")
    message = input("Input: ")
    appendFile.write(username)
    appendFile.write(" Entered: ")
    appendFile.write(message)
    appendFile.write(" | Written on --> ")
    appendFile.write(str(datetime.datetime.now()))
    appendFile.write('\n')
    appendFile.close()

for i in range(2):
    usr = input("Username: ")
    i = 2
    if(usr == username):
        print("Username is correct!")
        break
    else:
        logging.debug('Failed User Login ' + str(datetime.datetime.now()))
        sys.exit("Please try again later")
        continue

for i in range(3):
    pwd = input("Password: ")
    j=3
    if(pwd == password):
        print("welcome!")
        logging.debug('Successful User Login ' + str(datetime.datetime.now()))
        Append()
        break
    else:
        logging.debug('Failed User Login ' + str(datetime.datetime.now()))
        sys.exit("Please try again later")
        continue