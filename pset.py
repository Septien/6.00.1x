# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 19:29:26 2016

@author: Phantom

Problem set 2.
Problem 2.
Write a program that calculates he minimum fixed monthly payment needed in 
order pay off a credit card balance within 12 months. By a fixed monthly payment, 
we mean a single number which does not change each month, but instead is a constant 
amount that will be paid each month.
"""

def fpccBalance(balance, annualInterestRate):
    """
    Calculates the minimum monthly payment that pay off the debt in one year
    balance: int or float. Indicate the oustanding balance of the credit card
    annualInterestRate: float. annual interes rate as decimal.
    """
    ub = balance                    #unpaid balance
    mir = annualInterestRate / 12.0 #Monthly payment rate
    fp = 10                         #fixed pay, start with 10
    nub = 0
    paid = False                    #Is debt paid off?
    
    #Calculate the minimum monthly payment
    while not paid:
        #The original fixed pay works?
        for i in range(12):
            #caculate new outsatanding balance, unpaid balance - fixed pay
            nub = ub - fp
            #calculate new debt
            ub = (1 + mir) * nub
        
        #Is debt zero?
        if ub > 0:
            #No, it is not. Try again with a new fixed pay
            fp += 10
            ub = balance
        else:
            #yes, it is
            paid = True
    
    #return fixed pay
    return fp
    
fp = fpccBalance(3329, 0.2)
print ("Lowest payment: " + str(fp))