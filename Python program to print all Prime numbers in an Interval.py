# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 09:17:36 2020

@author: Akash Kaushik
"""


def user_input():
    
    number = "Wrong"
    
    while number.isdigit() == False:
        number = input()
        
        if number.isdigit() == False:
            print("Sorry ! Provide correct Input!")
            
    return int(number)

print("Enter the First Number: ")
a = user_input()

print("Enter the sec. Number: ")
b = user_input()

def check_prime(a,b):

    for num in range(a, b):
        if num > 1:
            for i in range(2,num):
                if(num % i) == 0:
                    break
            else:
                print(num)
            
print("Prime number between", a, "and", b, ":")
check_prime(a,b)