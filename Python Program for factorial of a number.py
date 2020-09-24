# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 09:39:55 2020

@author: Akash Kaushik
"""
"Creating Function for Input"

def user_input():
    
    number = "Wrong"
    
    while number.isdigit() == False:
        number = input()
        
        if number.isdigit() == False:
            print("Sorry! That is not a Number!")
            
    return int(number)

print("Enter the Positive Number: ")

def factorial(a):
    
    b = 1
    
    while a > 0:
        
        b = b*a
        a = a-1
        
    return b

a = user_input()
x = factorial(a)

print("Factorial of {} = {}".format(a,x))