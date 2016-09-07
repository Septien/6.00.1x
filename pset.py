# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 19:29:26 2016

@author: Phantom

Problem Set 1
Problema 3

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your 
program should print:

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd',
then your program should print:

Longest substring in alphabetical order is: abc
"""
s = 'dggknvaakmllsseckbolln'
subs = ''
subs1 = ''
pos = 0
for char in s:
    if pos == 0:
        subs += char
        pos += 1
    else:
        if char >= subs[pos - 1]:
            subs += char
            pos += 1
        else:
            if len(subs) > len(subs1):
                subs1 = subs
                subs = ''
                subs += char
                pos = 1
            else:
                subs = ''
                subs += char
                pos = 1
if len(subs1) >= len(subs):
    print("Longest substring in alphabetical orderis: " + subs1)
else:
    print("Longest substring in alphabetical orderis: " + subs)