#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 17:55:51 2017

"""

"""
Problem 3
10.0/10.0 points (graded)
Implement a function that meets the specifications below.

For example, sum_digits("a;35d4") returns 12.
"""
def sum_digits(s):
    """ assumes s a string
       Returns an int that is the sum of all of the digits in s.
       If there are no digits in s it raises a ValueError exception. """
    sum = 0
    valueerrtot = 0
    for i in s:
        try:
            sum += int(i)
        except:
            valueerrtot += 1
    if valueerrtot != len(s):
        return sum
    else:
        raise ValueError
        
"""
Problem 4
15.0/15.0 points (graded)
Implement a function that meets the specifications below.

For example,

max_val((5, (1,2), [[1],[2]])) returns 5.
max_val((5, (1,2), [[1],[9]])) returns 9.
"""
def max_val(t):
    """ t, tuple
       Each element of t is either an int, a tuple, or a list
       No tuple or list is empty
       Returns the maximum int in t or (recursively) in an element of t """
    
    pool = []
    for elm in t:
        if type(elm) == int:
            pool.append(elm)
        else:
            pool.append(max_val(elm))
    return max(pool)

"""
Problem 5
15.0/15.0 points (graded)

For example,

cipher("abcd", "dcba", "dab") returns (order of entries in dictionary may not be the same) ({'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc')
"""

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    # Your code here
    cipher_dict = {}
    decoded = ""
    for item in range(len(map_from)):
        cipher_dict[map_from[item]] = map_to[item]
    for char in range(len(code)):
        if code[char] in cipher_dict.keys():
            decoded+=cipher_dict[code[char]]
    mytuple = tuple([cipher_dict, decoded])
    return mytuple

"""
Problem 6-1
15.0/15.0 points (graded)
You are given the following superclass. Do not modify this.

class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s

        
For example,
d1 = Bag()
d1.insert(4)
d1.insert(4)
print(d1)
d1.remove(2)
print(d1)
prints
4:2
4:2

For example,
d1 = Bag()
d1.insert(4)
d1.insert(4)
d1.insert(4)
print(d1.count(2))
print(d1.count(4))
prints
0
3
"""

class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        if e in self.vals.keys():
            self.vals[e] -= 1
        else:
            return

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        if e in self.vals.keys():
            return self.vals[e]
        else:
            return 0
    def __add__(self, other):
        dict_copy = self.__class__()
        dict_copy.vals.update(self.vals)
        for value,count in other.vals.items():
            for _ in range(count):
                dict_copy.insert(value)
        return dict_copy
    
"""
Problem 6-2
5.0/5.0 points (graded)
Write a method in Bag such that if b1 and b2 were bags then b1+b2 gives a new bag representing the union of the two bags.

For example,
a = Bag()
a.insert(4)
a.insert(3)
b = Bag()
b.insert(4)
print(a+b)
prints
3:1
4:2
"""
class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        if e in self.vals.keys():
            self.vals[e] -= 1
        else:
            return

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        if e in self.vals.keys():
            return self.vals[e]
        else:
            return 0
    def __add__(self, other):
        dict_copy = self.__class__()
        dict_copy.vals.update(self.vals)
        for value,count in other.vals.items():
            for _ in range(count):
                dict_copy.insert(value)
        return dict_copy
    
"""
Problem 6-3
15.0/15.0 points (graded)
Write a class that implements the specifications below. Do not override any methods of Container.

class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        # write code here

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        # write code here

For example,
d1 = ASet()
d1.insert(4)
d1.insert(4)

d1.remove(2)
print(d1)

d1.remove(4)
print(d1)
prints
4:2 # from d1.remove(2) print

    # (empty) from d1.remove(4) print
For example,
d1 = ASet()
d1.insert(4)
print(d1.is_in(4))
d1.insert(5)
print(d1.is_in(5))
d1.remove(5)
print(d1.is_in(5))
prints
True
True
False
"""
class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        if e in self.vals.keys():
            del self.vals[e]
        else:
            return

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        if e in self.vals.keys():
            return True
        else:
            return False
        
"""
Problem 7
20.0/20.0 points (graded)
You are given the following two classes.

### Do not change the Location or Campus classes. ###
### Location class is the same as in lecture.     ###
class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def dist_from(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist**2 + yDist**2)**0.5
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'
        
class Campus(object):
    def __init__(self, center_loc):
        self.center_loc = center_loc
    def __str__(self):
        return str(self.center_loc)
Implement a class that meets the specifications below.

class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """
    def __init__(self, center_loc, tent_loc = Location(0,0)):
        """ Assumes center_loc and tent_loc are Location objects 
        Initializes a new Campus centered at location center_loc 
        with a tent at location tent_loc """
        # Your code here
      
    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance 
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """
        # Your code here
      
    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus. 
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        # Your code here
      
    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain 
        the string representation of the Location of a tent. The list should 
        be sorted by the x coordinate of the location. """
        # Your code here
For example, if c = MITCampus(Location(1,2)) then executing the following sequence of commands:

c.add_tent(Location(2,3)) should return True
c.add_tent(Location(1,2)) should return True
c.add_tent(Location(0,0)) should return False
c.add_tent(Location(2,3)) should return False
c.get_tents() should return ['<0,0>', '<1,2>', '<2,3>']
"""
class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """
    
    def __init__(self, center_loc, tent_loc = Location(0,0)):
        """ Assumes center_loc and tent_loc are Location objects 
        Initializes a new Campus centered at location center_loc 
        with a tent at location tent_loc """
        Campus.__init__(self, center_loc)
        self.tent_loc = [tent_loc]
      
    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance 
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """
        
        if all(new_tent_loc.dist_from(i) >= 0.5 for i in self.tent_loc):
            self.tent_loc.append(new_tent_loc)
            return True
        else:
            return False
        
    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus. 
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        if tent_loc in self.tent_loc:
            self.tent_loc.remove(tent_loc)
        else:
            raise ValueError
      
    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain 
        the string representation of the Location of a tent. The list should 
        be sorted by the x coordinate of the location. """
        tents = []
        for i in self.tent_loc:
            tents.append(i.__str__())
        return sorted(tents)