# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:54:24 2020

@author: Akash Kaushik
"""


def user_input():
    number = "Wrong"
    
    while number.isdigit() == False:
        
        number = input("Enter the positive n-th number:")
        
    return int(number)

num = user_input()

a = 0
b = 1

print("Fibonacci number:")
print(a)
print(b)



for i in range(0,(num-2)):
    c = a+b
    print(c)
    a = b
    b = c
    
