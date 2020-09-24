# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:30:32 2020

@author: Akash Kaushik
"""

def user_input():
    number = "Wrong"
    
    while number.isdigit() == False:
        number = input("Enter the positive Number: ")
        
    return int(number)

a = user_input()

b = True
def check_prime(a,b):

    while b:
        if a > 1:
            for j in range(2, int(a/2)):
                if (a % j)== 0:
                    b = False
                
    return b

    
if b == True:
    print (a, " is Prime Number")
else:
    print(a, "is Not Prime Number")
        
        
check_prime(a,b)
