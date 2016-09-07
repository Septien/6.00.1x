# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 19:29:26 2016

@author: Phantom

Problem Set 1
Problema 2

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
"""
s = 'ibobobboboboolciobobbobbbobbbo'
count = 0
l = len(s)
for i in range(l):
    if i + 1 >= l or i + 2 >= l:
        break
    if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
        count += 1
print ("Number of times bob occurs is: " + str(count))
