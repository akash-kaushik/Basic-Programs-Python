# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 08:47:49 2020

@author: Akash Kaushik
"""

"""
Creating function for taking input and 
Checking the input is in correct formet or not

"""

def user_input():
    
    number = "Wrong"
    
    while number.isdigit() == False:
        
        number = input()
        
        if number.isdigit() == False:
            print("Sorry! that is not a Number!")
            
    return int(number)

print("Enter only Positive number!")

print("First Number:")
a = user_input()

print("\nSecond Number:")
b = user_input()

c = a + b
print("\nSum = {}".format(c))
    
    