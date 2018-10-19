# -*- coding: utf-8 -*-
'For password generator'
__author__='Alex Meow'
#I'll add GUI later if I remeber to...with TkInter I guess.
import random
import string
import datetime
from time import sleep 
currenttime = str(datetime.datetime.now())
print(currenttime)

use = input("What do you use this for?(Username)\n")
digits =int(input('How many digits do you want?\n'))
lib = string.ascii_letters + string.digits+string.digits+string.digits
a= ''
b=0
while digits>0:
    b = random.choice(lib)
    a = a+b
    digits -=1

file = open ('catPassword.txt', 'a+')
file.write ('Time:' + currenttime + '  '+ use+' password is:  '+ a+ '\n' )
file.close()
file = open('catPassword.txt', 'r')
word = file. readlines()
file.close()
print (word[-1])
sleep(1)
print('Your password is stored in catPassword.txt file.\nOpen it to copy and paste')
sleep(600)
