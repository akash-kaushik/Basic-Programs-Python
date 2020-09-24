# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 09:59:55 2020

@author: Akash Kaushik
"""


def user_input():
    
    number = "Wrong"
    
    while number.isdigit() == False:
        number = input()
        
        if number.isdigit() == False:
            print("Sorry! Please provide a valid Input")
            
    return int(number)

print("Enter the Principal amount:")
p = user_input()

print("Enter the Annual Interest Rate:")
r = user_input()

print("Enter the Time(In Years):")
t = user_input()

si = (p*r*t)/100

print("Simple Interest = {}".format(si))
    
    