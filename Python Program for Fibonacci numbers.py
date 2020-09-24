# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:03:06 2020

@author: Akash Kaushik
"""


def user_input():
    
    number= "wrong"
    
    while number.isdigit() == False:
        number = input("Enter the positive number:")
        
    
    return int(number)

num = user_input()

a = 0
b = 1

if num == 1:
    print(a)

elif num == 2:
    print(b)
    
else:
    for i in range(2, num):
        c = a+b
        a = b
        b = c
    
    print(c)