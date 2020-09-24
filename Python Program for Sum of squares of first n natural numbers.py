# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 09:44:47 2020

@author: Akash Kaushik
"""

def user_input():
    
    number = "wrong"
    
    while number.isdigit() == False:
        number = input("Enter the Natural Number:")
        
    return int(number)

num = user_input()

def sum_natural(num):
    sum1 = 0
    for i in range(1, num+1):
        a = i*i
        sum1 = sum1 + a
    
    return sum1

b = sum_natural(num)

print("Sum of ", num, "natural number is", b)