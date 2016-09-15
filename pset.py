# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 19:29:26 2016

@author: Phantom

Problem set 2.
Problem 1.
Write a program that calculates the credit car balance after one 
year if a person only pays the minimum monthly payment required by 
the credit card company.
"""
def ccBalance(balance, annualInterestRate, monthlyPaymentRate):
    """
    balance: int or float. Indicate the oustanding balance of the credit card
    annualInterestRate: float. annual interes rate as decimal.
    monthlyPaymentRate: minimum monthly payment rate as decimal.
    """
    ub = balance                #unpaid balance
    aIR = annualInterestRate
    mPR = monthlyPaymentRate
    mmPR = 0                    #minimum Monthly payment
    nub = 0
    tap = 0                     #Total ammount paid
    for i in range(12):
        #Calculate the month payment
        mmPR = ub * mPR
        #Calculate the outstanding balance
        nub = ub - mmPR
        #print("Month " + str(i+1) + " Remaining balance: " + str(round(nub, 2)))
        tap += nub
        #Calculate the new outstandig rate
        ub = nub + (aIR/12.0)*nub
    return ub
    
print("Remainning balance: " + str(round(ccBalance(484, 0.2, 0.04), 2)))