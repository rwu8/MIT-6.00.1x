#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 17:48:50 2017
"""

"""
Problem 4:
Write a function is_triangular that meets the specification below. 
A triangular number is a number obtained by the continued summation of 
integers starting from 1. For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., 
corresponding to 1, 3, 6, 10, etc., are triangular numbers.

"""
def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 1, 3, 6, 10, 
    etc., are triangular numbers.
    
    """
    item = 0
    if k == 1:
        return True
    for n in range(k):
        item = n * (n+1)/2
        if item == k:
            return True
    else:
        return False
    
"""
Problem 5:
Write a Python function that takes in a string and prints out a version of 
this string that does not contain any vowels, according to the specification 
below. Vowels are uppercase and lowercase 'a', 'e', 'i', 'o', 'u'.

For example, if s = "This is great!" then print_without_vowels will print 
Ths s grt!. If s = "a" then print_without_vowels will print the empty string .
"""
def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    # Your code here
    newstr = s
    vowels = ('a', 'e', 'i', 'o', 'u', 'A','E','I','O','U')
    for x in s:
        if x in vowels:
            newstr = newstr.replace(x,"")
    print(newstr)

"""
Problem 6:
Write a function that satisfies the following docstring:
For example, if

largest_odd_times([2,2,4,4]) returns None
largest_odd_times([3,9,5,3,5,3]) returns 9

"""
def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    # Your code here
    largest=  0
    dict = {}
    new_dict = {}
    for i in L:
        dict.setdefault(i,0)
        dict[i]= dict[i] + 1
    
    for k,v in dict.items():
        if v % 2 == 1:
            new_dict.setdefault(k,0)       
    
    for k,v in new_dict.items():
        largest = max(k for k, v in new_dict.items())
        return largest
    return

"""
Problem 7:
Write a function called dict_invert that takes in a dictionary with immutable values and returns the inverse of the dictionary. The inverse of a dictionary d is another dictionary whose keys are the unique dictionary values in d. The value for a key in the inverse dictionary is a sorted list (increasing order) of all keys in d that have the same value in d.

Here are two examples:

If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}
"""

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    #YOUR CODE HERE
    v = {}
    for key, value in sorted(d.items()):
        v.setdefault(value,[]).append(key)
    return v

"""
Problem 8:
Write a function called general_poly, that meets the specifications below. 
For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234 because 1∗103+2∗102+3∗101+4∗100.
"""
def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def to_apply (x):
        n = 0
        for i in L:
            n = x*n + i
        return n
    return to_apply


"""
Problem 9
Write a Python function that takes in two lists and calculates whether they are permutations of each other. The lists can contain both integers and strings. We define a permutation as follows:

the lists have the same number of elements
list elements appear the same number of times in both lists
If the lists are not permutations of each other, the function returns False. 
If they are permutations of each other, the function returns a tuple consisting of the following elements:

the element occuring the most times
how many times that element occurs
the type of the element that occurs the most times
If both lists are empty return the tuple (None, None, None). If more than one element occurs the most number of times, you can return any of them.
"""

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    # Your code here
   
    # If both lists are empty return the tuple (None, None, None). 
    if len(L1) == 0 and len(L2) == 0:
        return (None, None, None)
    # Returns False if L1 and L2 are not permutations of each other. 
    elif sorted(L1) != sorted(L2):
            return False
    else:
        maxim = max(set(L1), key=L1.count)
        count = 0
        for i in L1:
            if i == maxim:
                count+=1
        typ = type(maxim)
        return tuple([maxim, count, typ])