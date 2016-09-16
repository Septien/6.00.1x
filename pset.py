# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 19:29:26 2016

@author: Phantom

Problem set 2.
Problem 2.
Write a program that calculates he minimum fixed monthly payment needed in 
order pay off a credit card balance within 12 months. By a fixed monthly payment, 
we mean a single number which does not change each month, but instead is a constant 
amount that will be paid each month. Use bisection search
"""

def fpccBalance(balance, annualInterestRate):
    """
    Calculates the minimum monthly payment that pay off the debt in one year
    using bisection search.
    balance: int or float. Indicate the oustanding balance of the credit card
    annualInterestRate: float. annual interes rate as decimal.
    """
    def calculatefp(mpub, mplb, mir, b):
        """
        Calculate the fixed pay recursively.
        mpub: monthly payment upper bound, decimal.
        mplb: monthly payment lower bound, decimal.
        mir: monthly interest rate, decimal.
        b: balance, decimal
        """
        #Calculate fixed pay for given bounds
        fp = (mpub + mplb) / 2.0
        ub = b
        #Calculate balance after 12 months of payments
        #It must be zero if fp is the correct
        for i in range(12):
            #unpaid balance
            ub = ub -  fp
            ub *= (1 + mir)
        
        #Is our debt zero?
        if round(ub, 4) == 0:
            #it is!
            return fp
        else:
            #No, it's not
            #Our monthly payment war too big
            if ub < 0:
                return calculatefp(fp, mplb, mir, b)
            #Our monthly payment was too small
            else:
                return calculatefp(mpub, fp, mir, b)
            
    
    mir = annualInterestRate / 12.0 #Monthly payment rate
    #Calculate initial upper bound
    mpub = (balance * ((1 + mir) ** 12)) / 12.0
    #Calculate intial lower bound
    mplb = balance / 12.0
    return calculatefp(mpub, mplb, mir, balance)    
    
fp = fpccBalance(999999, 0.18)
print ("Lowest payment: " + str(round(fp, 2)))