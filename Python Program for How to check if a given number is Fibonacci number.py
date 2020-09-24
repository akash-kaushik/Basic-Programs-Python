# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 09:01:20 2020

@author: Akash Kaushik
"""



def user_input():
    
    number = "Wronog"
    
    while number.isdigit() == False:
        
        number = input("Enter the positive number:")
        
    return int(number)

num = user_input()

def is_perfect_square(num):
    
    import math
    
    x = int(math.sqrt(num))
    
    return x*x == num

def is_fibonacci(num):
    
    return is_perfect_square(5*num*num + 4) or is_perfect_square(5*num*num - 4)

if is_fibonacci(num) == True:
    print(num, "is Fibonacci number!")
    
else:
    print(num, "is not a Fibonacci number!")