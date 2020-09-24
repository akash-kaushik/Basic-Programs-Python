# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 10:45:56 2020

@author: Akash Kaushik
"""


def user_input():
    number = "Wrong"
    
    while number.isdigit() == False:
        number = input()
        
        if number.isdigit() == False:
            print("Please Enter number only!")
            
    return int(number)

print("Enter Positive number only:")
a = user_input()

b = len(str(a))

def check_number(a):
    sum1 = 0
    while a != 0:
        r = a % 10
        sum1 = sum1+ pow(r,b)
        a = a / 10
        a = int(a)
        
    return int(sum1)

c = check_number(a)

if a == c:
    print("isArmstrong Number")
    
else:
    print("is Not Armstrong Number")