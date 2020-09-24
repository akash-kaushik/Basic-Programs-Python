# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 10:24:26 2020

@author: Akash Kaushik
"""


def user_input():
    number = "Wrong"
    
    while number.isdigit() == False:
        number = input()
        
        if number.isdigit() == False:
            print("Sorry! Provide a correct Input")
            
    return int(number)

print("Enter the Principle Amount:")
p = user_input()

print("Enter the interest Rate:")
r = user_input()

print("Enter the Time(In Year's)")
t = user_input()

a = p*((1+(r/100))**t)

ci = a - p

print("Compound Interest: {}".format(ci))