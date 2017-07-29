#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 17:40:00 2017
"""

#Question 1
"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print:
    Number of vowels: 5
"""
count = 0
for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        count+=1
print('Number of vowels: ' + str(count))

#Question 2
"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""
l = len(s)
pattern = 'bob'
ct = 0

for c in range(len(s)):
	if s[c:c+3] == pattern:
		ct += 1
print('Number of times bob occurs is: ' + str(ct))

#Question 3
"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the 
letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. 
For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc
"""
temp_arr = [s[0]]
longest_arr = []
substr = ""
for x in range(0,len(s)-1):
    if ord(s[x]) <= ord(s[x+1]):
        #split string and move to array
        temp_arr.append(s[x+1])
        print(temp_arr)
        if len(temp_arr) > len(longest_arr):
            longest_arr = temp_arr
    else:
        if len(temp_arr) > len(longest_arr):
            longest_arr = temp_arr
        temp_arr = []
        temp_arr.append(s[x+1])

#re-join array to print longest array
substr = ''.join(longest_arr)
print('Longest substring in alphabetical order is: ' + substr)