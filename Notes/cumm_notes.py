import pickle
import sys
import time
import os
import platform
import logging

# Packages for this class: numpy, scipy, scikit-learn, matplotlib, pandas, pillow, graphviz

# Python Overview

# Comments:
# print('hello world')  <- '#' comments a function
# Numbers:
# floating point and integer
# Strings:
# Single quote, double quotes, multiple line comments

# Format method - construct a string using variables
A = 20
B = 'Mike'
print('{0} is {1} years old' .format(B, A))     # or
print(B + ' is ' + str(A) + ' years old')
print('{0:.3f}'.format(1.0/3))
print('{0:_^11}'.format('hello'))
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

# print() function - always ends with an invisible new line character
# can use 'end=' to specify other characters
print('a', end='')
print('b', end='')      # output is ab

# operators: + (plus), - (minus), * (multiply), ** (power), / (divide), // (divide and floor), % (modulo)
# bit-wise operators: <<, >>, & (AND), | (OR), ^ (XOR), ~ (invert)
# logic operators: <, >, <=, >=, !=, not, and, or

# evaluation order:
# lambda
# if else
# or
# and
# not x
# in, not in, is, is not, <, <=, ...,
# ^
# &
# <<, >>
# +, -
# *, /, //, %
# +x, -x, ~x
# **
# x[index], x[ind1:ind2], x(), x.attribute
# (expressions), [expressions], {key:value}, {expressions}

# control flow: if

A = 23
B = 23      # int(input('Enter an Integer:'))
if A == B:
    print('Congrats')
elif B < A:
    print('Lower than true value')
else:
    print('higher than true value')

# control flow: for

for i in range(1, 5):
    print(i)
else:
    print('done')
# Use break and continue

# Function


def print_max(a, b):
    if a > b:
        print(a, ' is maximum')
    elif a == b:
        print(a, ' is equal to ', b)
    else:
        print(b, ' is maximum')


print_max(3, 4)     # directly pass literal values to function

# global variables
x = 50


def func():
    global x
    print('x is ', x)
    x = 2
    print('Changed global x to ', x)

func()
print('Value of x is', x)

# VarArgs, * is a list (numbers), ** can be multiple lists or value-pairs


def total(a=5, *numbers, **phonebook):
    print('a', a)

    # iterate through all the items in tuple
    for single_item in numbers:
        print('single_item', single_item)

    # iterate through all the items in dictionary
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560)

# return and pass to function


def maximum(z, y):
    if z > y:
        return z
    elif z == y:
        return 'The numbers are equal'
    else:
        return y


print(maximum(2, 3))

# docstrings or documentation strings


def print_max(x, y):
    '''Prints the maximum of two numbers,
    The two values must be integers.'''

    # convert to integers if possible
    x = int(x)
    y = int(y)
    if x > y:
        print(x, ' is maximum')
    else:
        print(y, ' is maximum')


print_max(3, 5)
print(print_max, __doc__)

# modules - to reuse a set of functions and variables
# put these functions/variables in a file .py, i.e. a module
# import modules when needed - "from math import sqrt" print("Square root of 16 is{", sqrt(16))
# to make a module behave in different ways:
if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')
# built-in dir() function returns the list of names defined by a module or an object
# import sys
a = 5
dir()

# ADVANCED TOPICS

# data structures: to store a collection of related data items
# four built-in data structures in python: List, Tuple, dictionary, set

# List
# Object: class functions, class fields
# Use square brackets to create a list
# Member functions: len(). append(), sort()
# example: Shopping list
shopList = ['apple', 'mango', 'carrot', 'banana']
print('I have ', len(shopList), ' items to purchase.')
print('These items are: ', end=' ')
for item in shopList:
    print(item, end=' ')

print('\nI also have to buy rice.')
shopList.append('rice')
print('My shopping list is now', shopList)

print('I will sort my list now')
shopList.sort()
print('Sorted shopping list is', shopList)

print('The first item I will buy is', shopList[0])
oldItem = shopList[0]
del shopList[0]

print('I bought the', oldItem)
print('My shopping list is now', shopList)

# Tuple
# - immutable
# example:
zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

newZoo = 'monkey', 'camel', zoo         # parentheses not required
print('Number of cages in the new zoo is', len(newZoo))
print('All animals in the new zoo are', newZoo)
print('Animals brought from old zoo are', newZoo[2])
print('Last animal brought from old zoo is', newZoo[2][2])
print('Number of animals in the new zoo is', len(newZoo)-1+len(newZoo[2]))

# Dictionary
# A collection of key/value pairs: key (name), value (details)
# Only immutable objects (string) can be used as keys
# Both immutable and mutable objects can be used for value
# ex:
ab = {
    'Swaroop': 'swaroop@gmail.com',
    'Larry': 'larry@gmail.com',
    'Matsumoto': 'mat@gmail.com',
    'Spammer': 'spammer@gmail.com'
}
print("Swaroop's address is", ab['Swaroop'])

# deleting a key-value pair
del ab['Spammer']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))
for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

# adding a key-value pair
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])

# Sequence
# Lists, tuples, and strings are special cases of sequence
# Three operations: membership tests (in, not in), indexing operations ([index]), slicing (fetch a sub sequence)
# Ex:
shopList = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

# Indexing or 'Subscription' operation
print('Item 0 is', shopList[0])
print('Item 1 is', shopList[1])
print('Item 2 is', shopList[2])
print('Item 3 is', shopList[3])
print('Item -1 is', shopList[-1])
print('Item -2 is', shopList[-2])
print('Character 0 is', name[0])

# Slicing on a list
print('Item 1 to 3 is', shopList[1:3])
print('Item 2 to end is', shopList[2:])
print('Item 1 to -1 is', shopList[1:-1])
print('Item start to end is', shopList[:])

# Slicing on a string
print('Characters 1 to 3 is', name[1:3])

# Set
# Unordered collections of simple objects
# Operations: membership tests, subset of another set, intersection between two sets
# Ex:
bri = set(['brazil', 'russia', 'india'])
bric = bri.copy()
bric.add('china')
bric.issuperset(bri)        # evaluated to true
bri.remove('russia')
print(bri & bric )
print(bri.intersection(bric))  # same as above line

# References
# When you create an object and assign it to a variable, the variable name points to the memory address...
# where the object is stored
# Two variables might refer to the same address
# Ex:
shopList = ['apple', 'mango', 'carrot', 'banana']
myList = shopList       # myList is name pointing to same object
# copy by making a full slice
myList = shopList[:]        # if one item is removed from shopList, myList will be unchanged


# Strings
# Objects in the class 'str'. Check help(str)
# Useful member functions: .startswith(''), in. .find(''), .join()

# Object-Oriented programming
# Object-Oriented vs Procedure-Oriented
# Objects are instances of classes
# A Class (built-in or accustomed) might have fields and member functions


class Person:
    # init method overrides the default instance, __init__ is called when a class instance is declared
    # init is private
    def __init__(self, name):       # self means for the current class instance
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('Swaroop')
p.say_hi()

# Class variables vs Object variables
# A variable in a class might below to the class, shared by all its instances
# Or, exclusively belong to an object, i.e., object variables


class Robot:
    """Represents a robot with a name"""
    population = 0      # A class variable, counting the number of robots

    def __init__(self, name):
        self.name = name
        print("Initializing {}".format(self.name))

    def die(self):
        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(self.name))

    def say_hi(self):
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """Prints the current population"""
        print("We have {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()
Robot.how_many()

# Inheritance
# Superclass (base class) and subclass (derived class)
# Reuse parent classes' variables and member functions
# Ex: Base class: SchoolMember

class SchoolMember:
    """Represents any school member"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''Tell my details'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    """Represents a teacher"""

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
    """Represents a student"""
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

members = [t, s]
for member in members:
    member.tell()       # works for teachers and student

# Input and Output
# Interacting with users: take user's input and print out results
# Basic functions: input(), print()

# Files
# Reading and writing files: class file, and .read(), .readline(), write()
# Ex:
poem = '''\
Welcome to Data Structures
It is an interesting class
At least, I believe so
'''
f = open('test.txt', 'w')       # for opening writing
f.write(poem)           # write text to file
f.close()           # close the file

f = open('test.txt')            # if no mode is specified, read is assumed by default
while True:
    line = f.readline()
    if len(line) == 0:      # zero length indicates EOF
        break
    print(line, end='')
f.close()

# Pickle
# Read or write any plain python objects using the built-in pickle class

shoplistfile = 'shoplist.data'
shoplist = ['apple', 'mango', 'carrot']

f = open(shoplistfile, 'wb')    # write to the file
pickle.dump(shoplist, f)        # dump the object to a file
f.close()

del shoplist        # destroy the shoplist variable

f = open(shoplistfile, 'rb')        # read bacl frp, storage
storedList = pickle.load(f)         # load the object from the file
print(storedList)
f.close()

# Unicode
# While reading non-English text, one needs to specify a Unicode format
# A non-english String should start with 'u'

# Exceptions
# Deal with unexpected errors (file nonexistant, insufficient memory, etc)
# Handle exceptions using try...except statements
# Example:
try:
    text = input('Enter something -->')
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation')
else:
    print('You entered {}'.format(text))

# Raise self-defined exceptions to control program flows


class ShortInputException(Exception):
    '''A user-defined exception class.'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Enter something -->')
    if len(text) < 3:
        raise ShortInputException((len(text), 3))
except EOFError:
    print('WHy did you do an EOF on me?')
except ShortInputException as ex:
    print(('ShortInputException: The input was {0} long, expected at least {1}').format(ex.length, ex.atleast))
else:
    print('No exception was raised.')
finally:
    print('finally')

# Another common usage of finally is to close files

f = None
try:
    f = open("poem.txt")        # Our usual file-reading idiom
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        time.sleep(2)               # make sure it runs for a while
except IOError:
    print("Could not find file poem.txt")
except KeyboardInterrupt:
    print("!! You cancelled the reading from the file.")
finally:
    if f:
        f.close()
    print("(Cleaning up: Closed the file)")

# Release Resources: With
# Using 'with' statement to release resources automatically (similar with the try..catch..finally statement)
# Ex:
with open("poem.txt") as f:
    for line in f:
        print(line, end='')

# Standard libraries: sys
# System-specific functions
# import sys
print(sys.version_info)
sys.version_info.major == 3

# Standard libraries: logging
# Store debugging messages or other important messages
if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'), 'test.log')
print("Logging to", logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w',
)

logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")

# Passing tuples
# In functions, one might return more than one objects


def get_error_details():
    return 2, 'details'


errnum, errstr = get_error_details()
print(errnum, ',', errstr)

# Special methods:
# __init__(self, ...) - called before the newly created onject is returned
# __del__(self, ...) - called before the object is destroyed
# __str__(self) - called when we use the print function or when str() is used
# __It__(self, other) - called when the '<' is used
# __getitem__(self, key) - called when x[key] indexing operation is used
# __len__(self) - called when the built-in len() function is used for the sequence object

# Lambda - One can use lambda argument: expression to create a function object
# Func1 = lambda num: num*2

# Iterator and Generator
# a popular for-loop statement: for element in iterable:
# Many types of objects in python qualify as being iterable
# An iterator object manages an iteration through a series of values
# An iterable is an object that produces ab iterator via iter(obj)
# Any function would be a generator, yield a series of values (rather than return)


def fibonacci( ):
    a = 0
    b = 1
    while True:
        yield a     # report value, a, during this pass
        future = a + b
        a = b       # next value reported
        b = future

# Conditional expressions
# a compact grammar: conditional expression syntax

n = -10
if n >= 0:
    param = n
else:
    param = n * -1
print(param)
print(n if n >= 0 else -1*n)      # conditional expression

# Comprehension syntax
# Goals: produce a series of values based on the processing of another series
# To generate a list of squares of the numbers from 1 to n
# The following control structure:
# result = []
# for value in iterable:
#    if condition
#       result.append(expression)
# is equivalent to:
# result = [ expression for value in iterable if condition]
n = 10
squares = [ ]
for k in range(1, n+1):
    squares.append(k*k)
print(squares)
# or
squares = [k*k for k in range(1, n+1)]
print(squares)

# similar syntaxes can be applied to list, set, generator, and dictionary:
# list: [ k for k in range(1, n+1) ]
# set: {k for k in range(1, n+1) }
# generator: (k for k in range(1, n+1) )
# dictionary: {k:k for k in range(1, n+1) }

# Pseudo-random number
# Random numbers are numbers that are statistically random
# Sequential generation: the current number is based on one or multiple previous random numbers
# Seed: the starting number
# Useful functions: random(), randint(a,b), randrange(start,stop,step); choice(seq); shuffle(seq)


#addMatrix.py
# Program to add two matrices using nested loop
X = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
Y = [[5, 8, 1],
    [6, 7, 3],
    [4, 5, 9]]
result = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

for i in range(len(X)):         # iterate through rows
   for j in range(len(X[0])):           # iterate through columns
       result[i][j] = X[i][j] + Y[i][j]
for r in result:
   print(r)

# Data Structures and Algorithms
# Our goals:
# Appropriate data structures, representing the problem to solve
# A good algorithm that performs the solution in an infinite time
# We only care about two things: correctness and efficiency

# Run-time Analysis
# More data (n), more time needed
# The focus of run-time analysis: the relationship between the running time and the size of its input (n)

# Exact measure: Elapse TIme (calculate elapsed time in python)
from time import time
s = time()      # record the starting time
# run algorithm
e = time()      # record the ending time
elapsed = e - s
# limitations of experimental analysis
# need to run two algorithms using the same hardware with the same data
# need to implement completely two algorithms
# limited data
# alternative strategy is needed for theoretical analysis

# Efficiency Analysis
# Main idea: count the number of basic (primitive) operations needed for an algorithm
# - adding two numbers, assigning a variable to an object, calling a function...
# Calculate number of operations as a function of the input size
# Concentrate on the worst case

# Asymptotic analysis
# Asymptotic: No exact count of basic operations is needed
# Examples:


def findmax(data):
    biggest = data[0]       # initial value to beat
    for val in data:
        if val > biggest:
            biggest = val
        return biggest
# worst case: 1 + n + 2n + 1 operations
# denoted O(n), ignore the constants


def prefix_average1(s):
    """Return list such that, for all j, A[j] equals average of s[0], ..., s[j]."""
    n = len(s)
    A = [0] * n
    for j in range(n):
        total = 0
        for i in range(j + 1):
            total += s[i]
        A[j] = total / (j+1)
    return A


print(prefix_average1([1, 2, 3, 5, 7, 9, 10]))
# worst case: 1 + 1 + n * (n-1)/2 + 1 operations
# denoted by O(n^2)

# Formal definition: Big-Oh
# let f(n) denote the expressions about the amount of basic operations
# let g(n) be functions that maps positive integers to positive real numbers
# f(n) is O(g(n)) if there is a real constant n_0 >= 1 such that f(n) <= c*g(n), for n >= n_0
# There are 7 typically used functions for big-Oh
# O(1): constant
# O(log n): logarithmic growth
# O(n): linear growth
# O(n log n): loglinear growth
# O(n^2): quadratic growth
# O(n^3): cubic growth
# O(2^n): exponential growth


# Asymptotic Analysis: Examples


def prefix_average2(s):
    """Return list such that, for all k, A[j] equals average of s[0], ..., s[j]."""
    # O(n^2) time
    n = len(s)
    A = [0] * n         # create list of n zeros
    for j in range(n):
        A[j] = sum(s[0:j+1]) / (j + 1)          # record the average
    return A


print(prefix_average2([1, 2, 3, 5, 7, 9, 10]))


def prefix_average3(s):
    """Return list such that, for all k, A[j] equals average of s[0], ..., s[j]."""
    # O(n) time
    n = len(s)
    A = [0] * n         # create list of n zeros
    total = 0           # compute prefix sum as Ss[0] + s[1] + ...
    for j in range(n):
        total += s[j]           # update prefix sum to include s[j]
        A[j] = total / (j+1)                # compute average based on current sum
    return A


print(prefix_average3([1, 2, 3, 5, 7, 9, 10]))


# example 2
# 3-way joint problem: given three sequences of numbers, find if their joint set is empty
# assume no individual sequence has duplicate elements


def disjoint1(A, B, C):
    """Return True if there is no element common to all three lists."""
    # O(n^3) time
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False            # we found a common value
    return True         # if we reach this, the sets are disjoint


def disjoint2(A, B, C):
    """Return True if there is no element common to all three lists."""
    # O(n^2) time
    for a in A:
        for b in B:
            if a == b:          # only check C if we found match from A and B
                for c in C:
                    if a == c:          # and thus a == b == c
                        return False            # we found a common value
    return True         # if we reach this, sets are disjoint


# example 3: uniqueness problem
# given a sequence of n elements, ask if all elements of that sequence are distinct from each other


def unique1(s):
    """Return True if there are no duplicate elements in sequence s."""
    # O(n^2) time
    for j in range(len(s)):
        for k in range(j+1, len(s)):
            if s[j] == s[k]:
                return False            # found duplicate pair
    return True         # if we reach this, elements were unique


def unique2(s):
    """Return True if there are no duplicate elements in sequence s."""
    # Sort all elements in order O(n log n)
    temp = sorted(s)            # create a sorted copy of s
    for j in range(1, len(temp)):
        if s[j-1] == s[j]:
            return False            # found duplicate pair
    return True         # if we reach this, elements were unique


# Relevant concepts
# Big-Oh notation defines an upper-bound for the number of operations needed for performing an algorithm
# upper bound = 'less than or equal to'
# Big-Omega notation means "greater than or equal to' - lower bound
# Big-Theta means it grows at the same rate

# Conclusion
# Big-Oh is a widely used way to roughly quantify algorithm complexity
# 7 classical relationship functions
# Foundations of data structure course

import os

# Recursion

# A technique by which a function repetitively calls itself
# Designed for repetition tasks
# Important technique for dealing with complicated data structure
# Not every problem can be solved with a recursion algorithm

# Example: Factorial Function


def factorial(n):
    if n == 0:              # special case, other cases are built on top of the special case
        return 1
    else:
        return n * factorial(n-1)       # nested function call


print(factorial(10))

# Example: Binary Search
# Goal: Given a sequence of numbers, locate the target value
# For an unsorted sequence, the search could be done by sequential search, in O(n) time
# For a sorted sequence, one might design a more efficient algorithm
# Main idea: To locate a number x in a sequence y
# - compare the middle of the sequence, denotedb y y[mid], to x
# - if x = y[mid], done
# - if x < y[mid], locate x in first-half of the input sequence
# - if x > y[mid], locate x in the second-half od the input sequence

def binary_search(data, target, low, high):
    """Return True if target is found in indicated portion .
    The search only considers the portion from data[low] to data[high]"""
    if low > high:
        return False            # interval is empty, no match
    else:
        mid = (low + high) // 2
        if target == data[mid]:         # found a match
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid-1)          # recur on left portion
        else:
            return binary_search(data, target, mid+1, high)         # recur on right portion


# Example: File Systems
# System dictionaries (or folders) are organized ina recursive way
# Adding new files or detecting files/folders are essentially recursive operations
# Our goal: calculating cumulative disk space for a folder
# This is equal to the immediate disk space of this folder plus the cumulative disk space usages of any subfolders
# Useful functions:
# os.path.getsize(path)
# os.path.isdir(path)
# os.listdir(path)
# os.path.join(path, filename


def disk_usage(path):
    total = os.path.getsize(path)           # account for direct usage
    if os.path.isdir(path):         # if this is a directory,
        for filename in os.listdir(path):           # then for each child:
            childpath = os.path.join(path, filename)            # compose full path to child
            total += disk_usage(childpath)                  # add child's usage to total
    print('{-:<7}'.format(total), path)
    return total


disk_usage('/Users/Guest')


# Running time analysis
# Big-oh: The number of primitive operations
# For a recursive function is is equal to the number of activations of the function times the number of operations
# with the body of the function

# Ex: Factorial algorithm
# 2 basic operations, O(n)

# Ex: Binary search
# The number of operations within each recursion is a constant
# Whats the number of recursion? check number of candidate entries to be searched for each call
# call 1: the number of candidate entries is n
# call 2: n/2
# call 3: n/4
# call i: n/2^(i-1)
# An unsuccessful search will stop around r calls where r is the smallest integer that satisfies
# n/2^(r-1) < 1, or n < 2^(r-1)      ->  O(log n)

# Ex: Space usage
# Let n denote the number of file-system entries (folders or files)
# The function will be called n times
# Within each call, the running time is O(1) or O(n) depending on how the function .getsize(path) works
# O(n)

# Recursion
# How to design a recursive algorithm
# Step 1: clearly design the outputs of the recursive function
# Step 2: Deal with the base cases, which do not need recursion
# Step 3: Recur: make one or multiple recursive calls
# Within the body of a single activation, there might be one single recursive call, two calls, or multiple calls

# Fibonacci numbers implementation 1
# if n<=1, return n
# otherwise, f(n) = f(n-2) + f(n=1)
# time complexity is O(2^n)


def fibonaccione(n):
    """Return the nth fibonacci number."""
    if n <= 1:
        return n
    else:
        return fibonaccione(n-2) + fibonaccione(n-1)

# Bad implementation bc f(n) depends on f(n-1) and f(n-2), and f(n-1) will recalculate f(n-2)
# which means duplicate calls

# Implementation 2
# Let f(n) return a pair of fino numbers at the n-th and (n-1)th, denoted Fn and Fn-1
# if n<=1 return n
# otherwise, call f(n-1) to get the current pair fn-1, fn-2, and return (fn-1 + fn-2, fn-1)
# time complexity is O(n)


def fibonaccitwo(n):
    "Return pair of fibonacci numbers, f(n) and f(n-1)"
    if n <= 1:
        return(n, 0)
    else:
        (Fn1, Fn2) = fibonaccitwo(n-1)
        return (Fn1+Fn2, Fn1)


print(fibonaccitwo(10))


# Ex: Sum of a sequence
# Calculate the sum of a sequence S recursively
# Step 1: recursive function, f(s, n)
# - return the sum of the first n values in the sequence
# Step 2: base cases
# - if n = 1, return s[n]
# Step 3: Recur
# - otherwise, return f(s, n-1) + s[n]


def linear_sum(s, n):
    """Return the sum of the first n numbers of sequence s."""
    if n == 0:
        return 0
    else:
        return linear_sum(s, n-1) + s[n-1]


print(linear_sum([4, 3, 6, 2, 8, 9], 5))


# Ex: Reverse a sequence
# Goal: write a recursive function to reverse the numbers in a sequence
# Step 1: recursive function, f(s,n)
# - return a list of the first n numbers in the reverse order
# Step 2: base cases
# - if n=1, return [s[n]]
# Step 3: recur
# - otherwise, return [s[n], f(s, n-1)]
# time complexity is O(n)

def reverse2(s, n):
    if n == 1:
        return [s[0]]
    else:
        A = []
        A.append(s[n-1])
        A.extend(reverse2(s, n-1))
        return A


s = [4, 3, 6, 2, 8, 9, 5]
print(reverse2(s, 7))


import sys

# Array Sequences

# Sequence
# An important data structure - building blocks for other complicated data structures
# Python sequence data types: lists, tuples, str
# Common features: Seq[index], implemented as an array, addition/deletion/etc

# Memory usages
# Memory address
# Random Access Memory (RAM) - O(1) time
# One variable might refer to one value or a sequence of values stored in memory
# Memory size:
# - storing a unicode character in python: 16 bites or 2 bytes
# - the string 'California' needs an array of 20 bytes
# - using an integer to describe the location(or cell) of a character within the array
# Each cell of an array must use the same number of bytes

# Three key concepts
# 1. Referential Arrays
# 2. Compact Arrays
# 3. Dynamic Arrays

# 1. Referential Arrays
# Each cell of an array must use the same number of bytes
# Problem: To put all student names in the same array, issue is names have varying length and need different
# number of bytes to store in memory
# Solution: Array of object reference (i.e. memory locations pointing to the actual strings)
# Fundamental concept in Data Structures
# - one array might include the same object as multiple elements
# - one Object might be the elements of multiple arrays
# - while creating a slice of an array, N=S[2:5], a new list instance N is created to point to existing objects

# Shallow copy and deep copy
# Let A denote a list of class instances
# - B=A: No copy; An alias name is created, pointing to the same list instance as A; No New Lista created.
# – B=list(A): shallow copy; A new list instance created; pointing to the same instances
# – B=copy.deepcopy(A): deep copy; create a new list instance as well as new elements of the list.

# Let warmtones denote a list of objects, and each object is an instance of the COLOR class
# - palette=warmtones: No copy
# - palette = list(warmtones): shallow copy, a new list instance is created pointing to the same COLOR object
# - palette = copy.deepcopy(warmtones): deep copy, create a new list instance as well as new elements of the list

# While referencing immutable objects, e.g., counter = [0] * 8, all cells reference the same object
# Since this object of 0 is immutable, counter[2]+=1 will create a new object
# WHEN CREATING LIST OBJECT, WE ARE WORKING WITH REFERENCES

# 2. Compact Arrays
# The Python List is not memory-efficient
# - to store 1 million 64-bit integers, it needs ideally 64 m bits
# - if used referential arrays (e.g. list) we need to store a 64-bit memory address for each element of the array
# - the integer itself is stored somewhere else
# Compact Array class is 'array' in python, which can save these extra memories
# array('i', [2, 3, 5, 7, 11, 13, 17, 19])
# -> the first argument indicates the type of elements to store in the array ('i' is unsigned int)
# -> no user defined classes/types are supported by the module array

# 3. Dynamic Arrays
# Python str or tuple are immutable and the memory spaces needed are fixed and pre-allocated
# In contrast, Python list support dynamic features: appending new elements, deleting elements, etc
# How does the memory allocation work for Python lists?

# import sys
n = 20
data = []
for k in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append(None)
# .getsizeof() returns the size of the list instance, not the spaces used for storing individual elements
# for a 64-bit computer, 8-bytes are needed to store a single address!
# Start with an underlying size, increase its capacity at geometric rate


# Python Sequence Types: List, Tuple, Str
# List and Tuple classes:
# Tuple is immutable
# List has immutable operations which are identically same as the Tuple's operation in terms of efficiencies
# Operation and running time:
# len(data) - O(1)
# data[j] - O(1)
# data.count(value) - O(n)
# data.index(value) - O(k+1)
# value in data - O(k+1)
# data1 == data2 - O(k+1)
# data[j:k] - O(k-j+1)
# data1 + data2 - O(n1 + n2)
# c * data - O(cn)

# List also has mutable operations
# Operation and running time:
# data[j] = val - O(1)
# data.append(value) - O(1)*
# data.insert(k, value) - O(n-k+1)*
# data.pop() - O(1)*
# data.pop(j) - O(n-k)*
# del data[k] - O(n-k)*
# data.remove(value) - O(n)*
# data1.extend(data2) - O(n2)*
# data1 += data2 - O(n2)*
# data.reverse() - O(n)
# data.sort() - O(n log n)
# * means amortized, wont change the size of the object

# Str class
# Pattern matching: .find(), .index(), .count(), .replace(), .split()
# Composing new strings() efficiency is a big concern
# Example: given a string, remove all the characters that are not alphabetic characters (dont do this)
letters = 'ab c#d e3fdkj'
newletters = ''     # start with empty string
for c in letters:
    if c.isalpha( ):
        newletters += c     # concatenate alphabetic character
print(newletters)
# Str is immutable and newletters += c will create a new string instance
# The total number of operations needed: (1+2+3...+n), O(n^2)
# A better idea: using the dynamic array: list -> O(n)
letters = 'ab c#d e3fdkj'
newletters = ''     # start with empty string
for c in letters:
    if c.isalpha( ):
        newletters.append(c)            # append alphabetic character
print(''.join(newletters))
# Alternative way O(n):
letters = ''.join(c for c in letters if c.isalpha())
print(letters)


# Multi-dimensional Data
# Lists, tuples, and strings in Python are one-dimensional
# Multidimensional data or matrix are popular in applications
# - images, videos, FMRI scans, geographic information
# Python uses list of list to represent matrix
data = [[22, 18, 709, 5, 33], [45, 32, 830, 120, 750], [4, 880, 45, 66, 61]]

# Method 1: Constant times 3, times 2 -> 1 dimensional array
data = ([0]*3)*2
print(data)
# Method 2: Creates list, multiplied by 2 so 2 lists. References same object -> 2 dimensional array
data=[[0]*3]*2
print(data)
data[0][1] = 3      # when revised
print(data)
# prints [[0, 3, 0], [0, 3, 0]]
# Method 3: Ensure each cell of the primary list should reference an independent list
data = [[0]*3 for j in range(2)]
print(data)
data[0][1] = 3      # when revised
print(data)
# prints [[0, 3, 0], [0, 0, 0]]

# Example: ScoreBoard
# Maintain a list of top-scored individuals (names, scores)
# Supporting class: GameEntry


class GameEntry:
    """Represents one entry of a list of high scores."""
    def __init__(self, name, score):
        """Create an entry with given name and score"""
        self._name = name
        self._score = score

    def get_name(self):
        """Return the name of the peron for this entry."""
        return self._name

    def get_score(self):
        """Return the score of this entry"""
        return self._score

    def __str__(self):
        """Return string representation of the entry."""
        return '({0}, {1})'.format(self._name, self._score)


class Scoreboard:
    """Fixed-length sequence of high scores in non-decreasing order."""
    def __init__(self, capacity=10):
        """Initialize scoreboard with maximum given capacity. All entries are initially none."""
        self._board = [None] * capacity
        self._n = 0

    def __getitem__(self, k):
        """Return entry at index k."""
        return self._board[k]

    def __str__(self):
        """Return string representation of the high score list."""
        return '\n'.join(str(self._board[j]) for j in range(self._n))

    def add(self, entry):
        """Consider adding entry to high scores"""
        score = entry.get_score()
        # Does new entry qualify as a high score?
        # answer is yes if board is not full or score is higher than last entry
        good = self._n < len(self._board) or score > self._board[-1].get_scores()

        if good:
            if self._n < len(self._board):          # no score drops from list
                self._n += 1                        # so overall number increases
            # shift lower scores rightward to make room for new entry
            j = self._n - 1
            while j > 0 and self._board[j-1].get_score() < score:
                self._board[j] = self._board[j-1]   # shift entry from j-1 to j
                j -= 1                              # and decrement j
            self._board[j] = entry                  # when done, add new entry

            
            # Stacks and Queues

# Stacks - Data Structure
# Store a collection of entries that are inserted and removed according to the "last in, first out" principle
# Two operations: Push, Pop
# Why we need stacks:
# - IE: recently visited sites
# - Text editors: 'undo' edits that recently happened
# - chain of method calls in a language that supports recursion

# Python Stacks
# In python, abstract data type (ADT) is used to represent stacks
# An ADT specifies:
# - Data stored
# - Operations on the data
# - error conditions associated with operations

# The ADT for Stack
# The Stack ADT can be used to store arbitrary classes of objects
# Insertions and deletions follow the last-in, first-out scheme
# Main class operations:
# - push(object): inserts an element
# - object pop(): removes and returns the last inserted element

# How to implement Stacks
# One simple way is to use the Python list
# - .append()
# - .pop()
# Adaptor Design Pattern: disable the behaviors of list not compatible with Stacks


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self._data = []             # nonpublic list instance

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)        # new item stored at end of list

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty"""
        if self.is_empty():
            # raise Empty('Stack is empty')
        return self._data[-1]       # the last item in the list

    def pop(self):
        """Remove and return the element from the top of the stack (LIFO).
        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            # raise Empty('Stack is empty')
        return self._data.pop()     # remove last item from list


# Performance and Limitations
# Performance:
# - Let n be the number of elements in the stack
# - The space used is O(n)
# 0 Each operation runs in time O(1) (Amortized in the case of a push)

# Applications of Stacks - Parentheses Matching and HTML tags Matching
# Parenthesis matching: Each "(", "{", or "[" must be matched with ")", "}", or "]"

# Parenthesis Matching Algorithm
# Algorithm ParenMatch(X,n):
# Input: An array X of n tokens, each of which is either a grouping symbol, a
# variable, an arithmetic operator, or a number
# Output: true if and only if all the grouping symbols in X match
# Let S be an empty stack
# for i=0 to n-1 do
#   if X[i] is an opening grouping symbol then
#       S.push(X[i])
#   else if X[i] is a closing grouping symbol then
#       if S.is_empty() then
#           return false {nothing to match with}
#       if S.pop() does not match the type of X[i] then
#           return false {wrong type}
# if S.isEmpty() then
#   return true {every symbol matched}
# else return false {some symbols were never matched}

# In python:


def is_matched(expr):
    """Return True if all delimiters are properly matched; False otherwise."""
    lefty = '({['
    righty = ')}]'
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.infex(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()


# HTML Tag Matching
# For fully-correct HTML, each <name> should pair with a matching </name>
# Tag matching algorithm in Python


def is_matched_html(raw):
    """Return True if all HTML tags are properly matched; False otherwise."""
    S = ArrayStack
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<', k+1)
    return S.is_empty()


# Queues - Data Structure
# Store a collection of entries
# - being inserted into or deleted from the collection: first in, first out

# ADT for Queues
# Two operations:
# - .enqueue(e): add an element to the back
# - .dequeue(e): remove an element from the front

# Implement Queues in Python
# Using the list class
# - .enqueue() -> list.append()
# - .dequeue() -> list.pop(0)
# Issue: .pop(0) is not efficient, since it will shift all the rest of the elements to the left, O(n)
# Solution: introduce a variable to indicate the start of the queue (not starting from 0)
# New issue: drifting away while enqueue/dequeue multiple times
# Solution: use the list circularly


class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10       # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue"""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        if self.is_empty():
            # Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            # raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None      # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))       # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):                 # assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        old = self._data                    # keep track of existing list
        self._data = [None] * cap           # allocate list with new capacity
        walk = self._front
        for k in range(self._size):         # only consider existing elements
            self._data[k] = old[walk]       # intentionally shift indices
            walk = (1 + walk) % len(old)    # use old size as modulus
        self._front = 0                     # front has been realigned


# Double Ended Queues
# Queue: First in, First out
# Double Ended Queues: In/out on both ends

# Linked List - Data Structure
# Like Python List, linked list also stores a collection of elements
# However, linked list doesn't need a large chunk of memory space
# - its elements (called nodes) are distributed and linked together to form a data structure

# Singly Linked List
# A singly linked list is a concrete data structure consisting of a sequence of nodes, starting from a head pointer
# Each node stores
# -> element
# -> link to the next node

# Singly Linked List example:
# - Nodes: Strings for airport names
# - Head: reference for first node
# - Tail: reference for last node
# - Traverse: following the links to visit every node

# Three Operations:
# 1. Inserting at the head
# 2. Removing at the head
# 3. Inserting at the tail

# Inserting at the head
# 1. Allocate a new node
# 2. Insert new element
# 3. Have new node point to old head
# 4. Update head to point to old node

# Removing at the head
# 1. Update head to point to next node in the list
# 2. Allow garbage collector to reclaim the former first node

# Inserting at the tail
# 1. Allocate a new node
# 2. Insert new element
# 3. Have new node point to null
# 4. Have old last node point to new node
# 5. Update tail to point to new node

# Stack as a Linked List
# Implement a stack with a singly linked list
# The top element is stored at the first node of the list
# The space used is O(n) and each operation of the Stack ADT takes O(1) time

# Linked-List Stack in Python


class LinkedStack:
    """LIFO Stack Implementation using a singly linked list for storage"""

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ == '_element', '_next'    # streamline memory usage

        def __init__(self, element, next):  # initialize node's fields
            self._element = element         # reference to user's element
            self._next = next               # reference to the next node

    def __init__(self):
        """Create an empty stack."""
        self._head = None       # reference to the head node
        self._size = 0          # number of stack elements

    def __len__(self):
        """Return the number of elements in the stack"""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty"""
        return self._size == 0

    def push(self, e):
        """Add an element e to the top of the stack."""
        self._head = self._Node(e, self._head)      # create and link a new node
        self._size += 1

    def top(self):
        """ Return (but do not remove) the element at the top of the stack.
        Raise empty exception if the stack is empty. """
        if self.is_empty():
            # raise Empty('Stack is empty')
        return self._head._element          # top of stack is at head of list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO)
        Raise EMpty exception if the stack is empty."""
        if self.is_empty():
            # raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        return answer


# Algorithm efficiency: Excellent
# The following operations all have O(1) running time
# S.push(e), S.pop(), S.top(), len(S), S.is_empty()


# Queue as a Linked List
# Implement a queue with a singly linked list
# - the front element is stored at the first node
# - the rear element is stored at the last node
# The space used is O(n) and each operation of the Queue ADT takes O(1) time

# Linked-List Queue in Python


class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ == '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):  # initialize node's fields
            self._element = element  # reference to user's element
            self._next = next  # reference to the next node

    def __init__(self):
        """Create an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0          # Number of queue elements

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return true if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty():
            # raise Empty('Queue is empty')
        return self._head._element          # front aligned with head of list

    def dequeue(self):
        """Remove and return the first element of the queue (i.e. FIFO).
        Raise Empty exception if the queue is empty."""
        if self.is_empty():
            # raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def dequeue(self, e):
        """Add an element to the back of queue."""
        newest = self._Node(e, None)        # node will be new tail node
        if self.is_empty():
            self._head = newest             # special case: previously empty
        else:
            self._tail._next = newest
        self._tail = newest                 # update reference to tail node
        self._size += 1


# Doubly linked list
# A doubly linked list provides a natural implementation of the Node List ADT
# Nodes implement Position and store:
# - element
# - link to the previous node
# - link to the next node
# There are special trailer and header nodes
# Insertion: insert a new node, q, between p and its successor
# Deletion: remove a node, p, from a doubly-linked list


class _DoublyLinkedBase:
    """A base class for providing a doubly linked list representation."""

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ == '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):  # initialize node's fields
            self._element = element  # reference to user's element
            self._next = next  # reference to the next node

    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer          # trailer is after header
        self._trailer._prev = self._header          # header is before trailer
        self._size = 0                              # number of elements

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, successor)          # linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Delete nonsentiel node from the list and return its element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element         # record deleted element
        node._prev = node._next = node._element = None      # deprecate node
        return element          # return deleted element

# Double linked list performance
# The space used bt a list with n elements is O(n)
# The space used by each position of the list is O(1)
# All the standard operations of a list run in O(1) time


# Positional Linked List
# To describe the position of a list element, one might use an index of integer
# - an element's index might change over time after addition/deletion
# Idea: Introduce a class Position to describe the position of an element
# - e.g., 'delete the character at the cursor'
# Positional List: includes a general abstraction class to identify the positions of its list elements


class Position:
    """An abstraction representing the location of a single element."""

    def __init__(self, container, node):
        """Constructor should not be invoked by user."""
        self._container = container
        self._node = node

    def element(self):
        """Return the element stored at this Position."""
        return self._node._element

    def __eq__(self, other):
        """Return True if other is a Position representing the same location."""
        return type(other) is type(self) and other._node is self._node

    def __ne__(self, other):
        """Return True if other does not represent the same location."""
        return not (self == other)      # opposite of __eq__

# Class instance p of Position: p.element(), returns the lement stored at this position
# - A position p is unaffected by changes elsewhere in a list
# - The only way in which a position becomes invalid is if an explicit command is issued to delete it
# This class serves as parameters for some of the List Operations

class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""

    class Position:
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)  # opposite of __eq__

    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:           # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinel."""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        """Return first Position in the list (or None if list is empty)."""
        return self._make_position(self._header._next)

    def last(self):
        """Return the last Position in the list (or None if list is empty)"""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """Return the Position just before Position p (or None if p is first)."""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """Return the Position just after Position p (or None if p is last)."""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    # Override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        """Add element e between existing nodes and return new Position."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert element e at the front of the list and return new Position."""
        return self._insert._between(e, self._header, self._header._next)

    def add_last(self, e):
        """Insert element e at the back of the list and return new Position."""
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """Insert element e into list before Position p and return new Position."""
        original = self._validate(p)
        return self._insert._between(e, original._prev, original)

    def add_after(self, p, e):
        """Insert element e into list after Position p and return new Position."""
        original = self._validate(p)
        return self._insert._between(e, original, original._next)

    def delete(self, p):
        """Remove and return the element as Position p."""
        original = self._validate(p)
        return self._delete_node(original)          # inherited method returns element

    def replace(self, p, e):
        """Replace the element at Position p with e.
        Replace the element formerly at Position p"""
        original = self._validate(p)
        old_value = original._element           # temporarily store old element
        original._element = e                   # replace with new element
        return old_value                        # return the old element value


# Examples
# Data Sorting
# Three variables:
# - marker: the right end of the sorted part
# - pivot: the next element to sort
# - walk: moving from the marker to the left while the walk's value is larger than the pivot


def insertion_sort(L):
    """Sort PositionalList of comparable elements into nondecreasing order."""
    if len(L) >1:                       # otherwise, no need to sort it
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)     # next item to place
            value = pivot.element()
            if value > marker.element():    # pivot is already sorted
                marker = pivot              # pivot becomes new marker
            else:                           # must relocate pivot
                walk = marker               # find leftmost item greater than value
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)   # reinsert value before walk


# Frequent Item List
# Program Goals: maintain a collection of items and their access frequencies
# - A web browser that keeps track of a user's most accessed URLS
# - Music collection that maintains a list of mostly played songs for a user
# Class Abstract Data Structure:
# .access(e): access the element e, increase its recent access, and add it to the list if not
# .remove(e): remove e from the list
# .top(k): return the top k elements from the list

# Example:
# This is a typical application of the sorted list
# after accessing an element, update the list to maintain the order
# items of List: class _Item

class FavoritesList:
    """List of elements ordered from most frequently accessed to least."""

    class _Item:
        __slots__ = '_value', '_count'  # streamline memory usage

        def __init__(self, e):
            self._value = e  # user's element
            self._count = 0  # access count initially zero

    def _find_position(self, e):
        """Search for element e and return its Position (or None if not found)."""
        walk = self._data.first()
        while walk is not None and walk.element().value != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        """Move item at Position p earlier in the list based on access count."""
        if p != self._data.first():         # consider moving
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:         # must shift forward
                while walk != self._data.first() and cnt > self._data.before(walk).element()._count:
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))       # delete/reinsert

    def __init__(self):
        """Create an empty list of favorites."""
        self._data = PositionalList()           # will be list of _Item instances

    def __len__(self):
        """Return number of entries on favorites list."""
        return len(self._data)

    def is_empty(self):
        """Return True if list is empty."""
        return len(self._data) == 0

    def access(self, e):
        """Access element e, thereby increasing its access count."""
        p = self._find_position(e)                      # try to locate existing element
        if p is None:
            p = self._data.add_last(self._Item(e))      # if new, place at end
        p.element()._count += 1                         # always increment count
        self._move_up(p)                                # consider moving forward

    def remove(self, e):
        """Remove element e from the list of favorites."""
        p = self._find_position(e)           # try to locate existing element
        if p is None:
            self._data.delete(p)            # delete if found

    def top(self, k):
        """Generate sequence of top k elements in terms of access count."""
        if not 2 <= k <= len(self):
            raise ValueError('Illegal value for k')
        walk = self._data.first()
        for j in range(k):
            item = walk.element()           # element of list is _Item
            yield item._value               # report user's element
            walk = self._data.after(walk)


fav = FavoritesList()
for c in 'this is a test':
    fav.access(c)
    k = min(5, len(fav))
    print('Top {0} {1} '.format(k, [x for x in fav.top(k)] ))
    
    # Trees
# What is a Tree
# - in CS, a tree is an abstract model of a hierarchical structure
# - a tree consists of nodes with a parent-child relation
# - applications: organization charts, file systems, programming environments

# Tree Terminology
# - root: node without a parent
# - internal node: node with at least one child
# - external node (aka leaf): node without children
# - ancestors of a node: parent, grandparent, grand-grandparent, etc
# - depth of a node: number of ancestors
# - height of a tree: maximum depth of any node
# - descendant of a node: child, grandchild, grand-grandchild, etc
# - subtree: tree consisting of a node and its descendants

# Tree ADT
# We use positions to abstract nodes
# Generic methods:
# - Integer len()
# - Boolean is_empty()
# - Iterator positions()
# - Iterator iter()
# Accessor methods:
# - position root()
# - position parent(p)
# - iterator children(p)
# - integer num_children(p)
# Query methods:
# - Boolean is_leaf(p)
# - Boolean is_root(p)
# Update method:
# - element replace (p, o)
# Additional update methods may be defined by data structures implementing the Tree ADT

# Abstract Tree Class in Python
# - this is an ABSTRACT BASE CLASS
# - it includes a nested Position class to locate elements in the tree


class Tree:
    """Abstract base class representing a tree structure"""

    # Nested Position class
    class Position:
        """An abstraction representing the location of a single element."""

        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not(self, other)         # opposite of __eq__

    # Abstract methods that concrete subclass must support
    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """Return Positon representing p's parent (or None if p is root)."""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """Return the number of children that Position p has."""
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError('must be implemented by subclass')

    # Concrete methods implemented in this class
    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p does not have any children"""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

# Example 1: Calculating the depth of a tree
# for a node S:
# - if S is root node, its depth is 0
# - otherwise, its depth is 1+ its children's depth
# Design recursive algorithm for counting a node's depth


def depth(self, p):
    if self.is_root(p):
        return 0
    else:
        return 1 + self.depth(self.parent(p))

# Example 2: Calculating the height of a node
# The height of a node p in a tree is defined recursively
# - if p is a leaf node, its height is 0
# - otherwise, its height is one more than the maximum of the heights of p's children nodes

# implementation 1: ... for ... in ... if - O(n^2) worst-case time


def _height1(self):
    """Return the height of the tree."""
    return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

# implementation 2: O(n) worst-case time


def _height2(self, p):
    """Return the height of the subtree rooted at Position p."""
    if self.is_leaf(p):
        return 0
    else:
        return 1 + max(self._height2(c) for c in self.children(p))

# Example 3: Traverse a tree
# visiting all the nodes of a tree or subtree, one by one
# a recursive function, visit (S), where S is the root node for a tree or subtree
# - visit S
# - visit the children nodes of S
# This visiting strategy is called pre-order, since it visits the node S first and its children nodes second
# in a preorder traversal, a node is visited before its descendants
# Algorithm preOrder(v)
#    visit(v)
#    for each child w of v
#       preOrder(w)
# in postorder traversal, a node is visited after its descendants
# Algorithm postOrder(v)
#    for each child w of v
#       postOrder(w)
#    visit(v)
# breadth-first tree traversal: visiting the nodes at depth d before d+1
# it is not recursively defined
# Algorithm breadthfirst(T)
#    Initialize queue Q to contain T.root()
#    while Q not empty do
#       p = Q.dequeue()     // p is the oldest entry in the queue
#       perform the "visit" action for position p
#       for each child c in T.children(p) do
#       Q.enqueue(c)        // add p's children to the end of the queue for later visits

# Binary Trees
# A binary tree is a tree with the following properties:
# - each internal node has at most two children (exactly two for proper binary trees)
# - the children of a node are an ordered pair
# we call the children of an internal node left child and right child
# Alternative recursive definition: a binary tree is either
# - a tree consisting of a single node, or
# a tree whose root has an ordered pair of children, each of which is a binary tree

# BinaryTree ADT
# The BinaryTree ADT extends the Tree ADT, i.e., it inherits all the methods of the Tree ADT
# Update methods may be defined by data structures implementing the BinaryTree ADT
# Additional methods:
# - position left(p)
# - position right(p)
# - position sibling(p)

# InOrder Traversal
# Pre-Order and Post-Order Traversal are applicable
# In an in order traversal a node is visited after its left subtree and before its right subtree
# Application: draw a binary tree
# - x(v) = inorder rank of v
# - y(v) = depth of v
# Algorithm inOrder(v)
#   if v has a left child
#       inOrder(left(v))
#   visit(v)
#   if v has a right child
#       inOrder(right(v))

# BinaryTrees: Applications
# - arithmetic expressions
# - decision processes
# - searching

# Arithmetic Expression Tree
# Example: Arithmetic expression tree for the expression (2 x (a - 1) + (3 x b))
# - binary tree associated with an arithmetic expression
# - internal nodes: operators
# - external nodes: operands

# Print Arithmetic Expressions
# Specialization of an inorder traversal
# - print operand or operator when visiting node
# - print "(" before traversing left subtree
# - print ")" after traversing right subtree
# Algorithm printExpression(v)
#   if v has a left child
#       print("(")
#       inOrder(left(v))
#   print(v.element())
#   if v has a right child
#       inOrder(right(v))
#       print(")")

# Evaluate Arithmetic Expressions
# Specialization of a postorder traversal
# - recursive method returning the value of a subtree
# - when visiting an internal node, combine the values of the subtrees
# Algorithm evalExpr(v)
#   if is_leaf(v)
#       return v.element()
#   else
#       x <- evalExpr(left(v))
#       y <- evalExpr(right(v))
#       (diamond) <- operator stored at v
#       return x (diamond) y

# Decision Tree
# Binary tree associated with a decision process
# - internal nodes: questions with yes/no answer
# - external nodes: decisions
# Example: dining decision

# Properties of Proper Binary Trees
# Notation: n (number of nodes), e (number of external nodes), i (number of internal nodes), h (height)
# Properties:
# - e = i + 1
# - n = 2e - 1
# - h <= i
# - h <= (n-1)/2
# - e <= 2^h
# - h >= log2 (e)
# - h >= log2 (n+1) -1

# Euler Tour Traversal
# Generic traversal of a binary tree
# Includes a special case of the preorder, postorder, and inorder traversals
# Walk around the tree and visit each node three times:
# - on the left(preorder)
# - from below (inorder)
# - on the right (postorder

# Tree Implementation
# - Linked Structures
# - Array-based Structures

# Linked Structure for Trees
# A node is represented by an object storing:
# - element
# - parent node
# - sequence of children nodes
# Node objects implement the Position ADT

# Linked Structure for Binary Trees
# A node is represented by an object storing:
# - element
# - parent node
# - left child node
# - right child node
# Node objects implement the Position ADT

# Array-Based Representation of Binary Trees
# Nodes are stored in an array A
# Node v is stored at A[rank(v)]
# = rank(root) = 1
# - if node is the left child of parent(node)
# -     rank(node) = 2 * rank(parent(node))
# - if node is the right child of parent(node)
# -     rank(node) = 2 * rank(parent(node)) + 1

# Expression Tree Example
# Goal: a Python class that supports
# - construct expression trees
# - display the expression that a tree represents
# - evaluate the expression that a tree represents
# Python classes
# - Tree
# - BinaryTree(Tree)
# - LinkedBinaryTree(BinaryTree)
# - ExpressionTree(LinkedBinaryTree)

# Class Tree
# Abstract base class representing a general tree
# Nested class: Position, used to locate nodes in a tree

# Class BinaryTree
# Abstract base class representing a binary tree
# Two additional abstract methods:


def left(self, p):
    """Return a Position representing p's left child.
    Return None of P does not have a left child."""
    raise NotImplementedError('must be implemented by subclass')


def right(self, p):
    """Return a Position representing p's right child.
    Return None of P does not have a right child."""
    raise NotImplementedError('must be implemented by subclass')

# four methods implemented in this class


def sibling(self, p):
    """Return a Positon representing p's sibling (or None if no sibling)."""
    parent = self.parent(p)
    if parent is None:                      # p must be the root
        return None                         # root has no sibling
    else:
        if p == self.left(parent):
            return self.right(parent)       # possibly None
        else:
            return self.left(parent)        # possibly None


def children(self, p):
    """Generate an iteration of Positions representing p's children."""
    if self.left(p) is None:
        yield self.left(p)
    if self.right(p) is None:
        yield self.right(p)


def _subtree_inorder(self, p):
    """Generate an inorder iteration of positions in subtree rooted at p."""
    if self.left(p) is not None:            # if left child exists, traverse it
        for other in self._subtree_inorder(self.left(p)):
            yield other
    yield p                                 # visit p between its subtrees
    if self.right(p) is not None:           # if right child exists, traverse it
        for other in self._subtree_inorder(self.right(p)):
            yield other


def inorder(self):
    """Generate an inorder iteration of positions in the tree."""
    if not self.is_empty():
        for p in self._subtree_inorder(self.root()):
            yield p

# one method that overwrites the abstract method of Tree


def positions(self):
    """Generate an iteration of the tree's positions."""
    return self.inorder()           # make inorder the default


# Class LinkedBinaryTree
# Implement the BinaryTree class using Linked-based sequences
# nested _Node class

from .binary_tree import BinaryTree

class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure."""

    # nested _Node Class
    class Node:
        """Lightweight, nonpublic class for storing a node."""
        __slots__ = '_element', '_parent', '_left', '_right'        # streamline memory usage

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    # nested Position Class
    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

    # utility methods
    def _validate(self, p):
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong in this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None

    # binary tree constructor
    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None
        self._size = 0

    # public accessors
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    def root(self):
        """Return the root Position of the tree (or None if tree is empty)."""
        return self._make_position(self._root)

    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """Return the position of p's left child (or None if no left child)."""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Return the position of p's right child (or None if no right child)."""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        count = 0
        if node._left is not None:      # left child exists
            count +=1
        if node._right is not None:     # right child exists
            count += 1
        return count

    def _add_right(self, p, e):
        """Create a new right child for Position p, storing element e.
        Return the Position of new node.
        Raise ValueError if Position p is invalid, or p already has a right child."""
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)           # node is its parent
        return self._make_position(node._right)

    def _replace(self, p, e):
        """Replace the element at position p with e, and return old element."""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _attach(self, p, t1, t2):
        """Attach trees t1 and t2, respectively, as left and right subtrees of the external Position p
        As a side effect, set t1 and t2 to empty
        Raise TypeError if t1 and t2 do not match type of this tree.
        Raise ValueError if Position p is invalid or not external."""
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):      # all 3 trees must be same type
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():           # attached t1 as left subtree of node
            t1._root._parent = node
            node._left = t1._root
            t1._root = None             # set t1 instance to empty
            t1._size = 0
        if not t2.is_empty():           # attached t2 as right subtree of node
            t2._root._parent = node
            node._right = t2._root
            t2._root = None             # set t2 instance to empty
            t2._size = 0


# ExpressionTree
# Major methods
# - Tokenize(raw): that convert an original expression into a list of tokens, e.g., '(43-(3*10))' results in the list
# - ... ['(', '43', '-', '(', '3', '*', '10', ')', ')']
# - build_expression_tree(tokens): create a binary tree to represent the tokens
# - Evaluate(): return the numeric result of the expression

from .linked_binary_tree import LinkedBinaryTree

class ExpressionTree(LinkedBinaryTree):
    """An arithmetic expression tree."""

    def __init__(self, token, left=None, right=None):
        """Create an expression tree."""
        super().__init__()                                  # LinkedBinaryTree initialization
        if not isinstance(token, str):
            raise TypeError('Token must be a string')
        self._add_root(token)                               # use inherited, nonpublic method
        if left is not None:                                # presumably three-parameter form
            if token not in '+-*x/':
                raise ValueError('token must be valid operator')
            self._attach(self.root(), left, right)          # use inherited, nonpublic method

    def __str__(self):
        """Return string representation of the expression."""
        pieces = []         # sequence of piecewise strings to compose
        self._parenthesize_recur(self.root(), pieces)
        return ''.join(pieces)

    def tokenize(raw):
        """Produces list of tokens indicatedb y a raw expression string."""
        SYMBOLS = set('+-x*/90 ')       # allow for 'x' or '*' multiplication

        mark = 0
        tokens = []
        n = len(raw)
        for j in range(n):
            if raw[j] in SYMBOLS:
                if mark != j:
                    tokens.append(raw[mark:j])  # complete preceding token
                if raw[j] != ' ':
                    tokens.append(raw[j])       # include this token
                mark = j+1                      # update mark to being at next index
            if mark != n:
                tokens.append(raw[mark:n])      # complete preceding token
            return tokens

    def build_expression_tree(tokens):
        """Returns an ExpressionTree based upon by a tokenized expression."""
        S = []                                                      # use Python list as stack
        for t in tokens:
            if t in '+-x*/':                                        # t is an operator symbol
                S.append(t)                                         # push the operator symbol
            elif t not in '()':                                     # consider t to be a literal
                S.append(ExpressionTree(t))                         # push trivial tree storing value
            elif t == ')':                                          # compose a new tree from three constituent parts
                right = S.pop()                                     # right subtree as per LIFO
                op = S.pop()                                        # operator symbol
                left = S.pop()                                      # left subtree
                S.append(ExpressionTree(op, left, right))           # repush tree
            # ignore a left parenthesis
        return S.pop()

    def evaluate(self):
        """Return the numeric result of the expression."""
        return self._evaluate_recur(self.root())

    def _evaluate_recur(self, p):
        """Return the numeric result of subtree rooted at p."""
        if self.is_leaf(p):
            return float(p.element())
        else:
            op = p.element()
            left_val = self._evaluate_recur(self.left(p))
            right_val = self._evaluate_recur(self.right(p))
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            elif op == '/':
                return left_val / right_val
            else:
                return left_val * right_val

    big = build_expression_tree(tokenize('((((3+1)x3)/((9-5)+2))-((3x(7-4))+6))'))
    print(big, '=', big.evaluate())

    
# Priority Queues and Heaps

# Priority Queue
# Data structure Queue: first in, first out
# In applications, one might prioritize elements (based on different factors) for leaving the queue, e.g., 'out'
# Extend the Queue: adding a key to each element, representing its priority
# The element with highest priority (key) will be out first

# Priority Queue ADT
# A priority queue stores a collection of items
# Each item is a pair (key, value)
# Main methods of the Priority Queue ADT:
# - add (k,x): inserts an item with key k and value x
# - remove_min(): removes and returns the item with smallest key
# Additional methods:
# - min(): returns, but does not remove, an item with smallest key
# - len(P), is_empty()

# Keys: Total Order Relations
# Keys in a priority queue can be arbitrary objects on which an order is defined
# Two distinct entries in a priority queue can have the same key
# Mathematical concept of total order relation <=
# - relative property: x <= x
# - antisymmetric property: x <= y ^ y <= x  so x = y
# - transitive property: x <= y ^ y <= z  so x <= z

# Item: Key-Value Pairs
# An item in a priority queue is simply a key-value pair
# Priority queues store items to allow for efficient insertion and removal based on keys


class PriorityQueueBase:
    """Abstract base class for a priority queue."""

    class _Item:
        """Lightweight composite to store priority queue items."""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key       # compare items based on their keys

    def is_empty(self):
        """Return True if the priority queue is empty"""
        return len(self) == 0


# Priority Queue: Implementations
# Implementation with an unsorted list
# - performance:
# - add takes O(1) time since we can insert the item at the beginning or end of the sequence
# - remove_min() and min() take O(n) time since we have to traverse the entire sequence to find the smallest key
# Implementation with an sorted list
# - performance:
# - add takes O(n) time since we have to find the place where to insert the item
# - remove_min() and min() take O(1) time, since the smallest key is at the beginning

# Unsorted List Implementation


class UnsortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with an unsorted list."""

    def _find_min(self):        # non-public utility
        """Return Position of item with minimum key"""
        if self.is_empty():     # inherited from base class
            raise Empty('Priority queue is empty')
        small = self._data.first()
        walk = self.data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair."""
        self._data.add_last(self._Item(key, value))

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key."""
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key."""
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)


# Sorted List Implementation


class SortedPriorityQueue(PriorityQueueBase):       # base class defines _Item
    """A min-oriented priority queue implemented with a sorted list."""

    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair."""
        newest = self._Item(key, value)     # make new item instance
        walk = self._data.last()            # walk backward looking for smaller key
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)            # new key is smallest
        else:
            self._data.add_after(walk, newest)      # newest goes after walk

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key."""
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key."""
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        item = self._data.delete(self._data.first())
        return (item._key, item._value)


# Priority Queues for Sorting
# We can use a priority queue to sort a set of comparable elements
# 1. Insert the elements one by one with a series of add operations
# 2. Remove the elements in sorted order with a series of remove_min operations
# The running time of this sorting method depends on the priority queue implementation

# Algorithm PQ-Sort(S,C)
#    Input sequence S, comparator C for the elements of S
#    Output sequence S sorted in increasing order according to C
#    P <- priority queue with comparator C
#    while S,is_empty()
#        e <- remove_first()
#        P.add(e, )
#    while P.is_empty()
#       e <- P.removeMin().key()
#       S.add_last(e)

# Variant 1/2: Selection-Sort
# Selection-sort is the variation of PQ-sort where the priority queue is implemented with an unsorted sequence
# Running time of Selection-Sort
# 1. Inserting the elements into the priority queue with n insert operations takes O(n) time
# 2. Removing the elements in sorted order from the priority queue with n removeMin operations takes time proportional
#    to 1 + 2 + ... + n
# Selection-sort runs in O(n^2) time

# Variant 2/2: Insertion-Sort
# Insertion-sort is the variation of PQ sort where the priority queue is implemented with a sorted sequence
# Running time of Insertion-sort:
# 1. Inserting the elements into the priority queue with n insert operations takes time proportional to 1 + 2 + ... + n
# 2. Removing the elements in sorted order from the priority queue with a series of n removeMin operations takes O(n)
# Insertion-sort runs in O(n^2) time

# In-place Insertion-Sort
# Instead of using an external data structure, we can implement selection so-sort and insertion-sort in place
# A portion of the input sequence itself serves as the priority queue
# For in-place insertion-sort
# - we keep sorted the initial portion of the sequence
# - we can use swaps instead of modifying the sequence

# Heap
# A new implementation of the priority Queue
# - unsorted list: O(1) insertion, O(n) access
# - sorted list: O(1) access, O(n) insertion
# Heap is very different implement of the priority idea with logarithm complexity

# Heaps
# A heap is a binary tree sorting keys at its nodes and satisfying the following properties:
# - Heap-Order: for every internal node b other than the root, key(v) >= key(parent(v))
# - Complete Binary Tree: let h be the height of the heap
#    - for i = -, ..., h-1, there are 2^i nodes of depth i
#    - at depth h-1, the internal nodes are to the left of the external nodes
# The last node of a heap is the rightmost node of maximum depth

# Height of a heap
# Theorem: A heap storing n keys has height O(log n)
# Proof: (we apply the complete binary tree property)
# - let h be the height of a heap storing n keys
# - since there are 2^i keys at depth i=0, ..., h-1 and at least one key at depth h, we have n>=1+2+4+...+2^(h-1) + 1
# - thus, n >= 2^h , i.e., h<= log n

# Heaps and Priority Queues
# we can use a heap to implement a priority queue
# we store a (key, element) item at each internal node
# we keep track of the position of the last node

# Heap: Operations/Algorithms
# 1. Insertion
# 2. Upheap
# 3. Removal from a heap
# 4. Downheap
# 5. Updating the last node
# 6. Heap-Sort
# 7. Array-based implementation
# 8. Merging two heaps
# 9. Heap Construction

# 1. Insertion into a heap
# Method add of the priority queue ADT corresponds to the insertion of a key k to the heap
# The insertion algorithm consists of three steps
# - find the insertion node x (the last node)
# - store k at z
# - restore the heap-order property (discussed next)

# 2. Upheap
# After the insertion of a new key k, the heap-order property may be violated
# Algorithm upheap restores the heap-order property by swapping k along an upward path from the insertion node
# Upheap terminates when the key k reaches the root or a node whose parent has a key smaller than or equal to k
# Since a heap has height O(log n), upheap runs in O(log n) time

# 3. Removal from a Heap
# Method remove_min of the priority queue ADT corresponds to the removal of the root key from the heap
# The removal algorithm consists of three steps
# - replace the root key with the key of the last node w
# - remove w
# - restore the heap-order property (discussed next)

# 4. Downheap (to restore the heap order)
# After replacing the root key with the key k of the last nodem the heap-order property may be violated
# Algorithm downheap restores the heap-order property by swapping key k along a downward path from the root
# Upheap terminates when key k reaches a leaf or a node whose children have keys greater than or equal to k
# Since a heap has height O(log n), downheap runs in O(log n) time

# 5. Updating the Last Node
# Insertion node can be found by traversing a path of O(log n) nodes
# - go up until a left child or the root is reached
# - if a left child is reached, go to the right child
# Similar algorithm for updating the last node after a removal

# 6. Heap-Sort
# Consider a priority queue with n items implemented by means of a heap
# - the space used is O(n)
# - methods add and remove_min take O(log n) time
# - methods len, is_empty, and min take O(1) time
# Using a heap-based priority queue, we can sort a sequence of n elements in O(n log n)
# The resulting algorithm is called heap-sort
# Heap-sort is much faster than quadratic sorting algorithms, such as insertion-sort and selection-sort

# 7, Array-based implementation
# We can represent a heap with n keys by means of an array of length n
# For the node at rank i
# - the left child is at rank 2i + 1
# - the right child is at rank 2i + 2
# Links between nodes are not explicitly stored
# Operation add corresponds to inserting at rank n + 1
# Operation remove_min corresponds to removing at rank n
# Yields in-place heap-sort


class HeapPriorityQueue(PriorityQueueBase):         # base class defines _Item
    """A min-oriented priority queue implemented with a binary heap."""

    # nonpublic behaviors
    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2*j + 1

    def _right(self, j):
        return 2*j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        """Swap the elements at indices i and j of array."""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)        # recur at position of parent

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left                  # although right may be smaller
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
                if self._data[small_child] < self._data[j]:
                    self._swap(j, small_child)
                    self._downheap(small_child)                 # recur at position of small child

    # public behaviors

    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = []

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair to the priority queue."""
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)               # upheap newly added position

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.
        Raise Empty exception if empty."""
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        item = self._data[0]
        return item._key, item._value

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key.
        Raise Empty exception if empty."""
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        self._swap(0, len(self._data) - 1)          # put minimum item at the end
        item = self._data.pop()                     # and remove it from the list
        self._downheap(0)                           # then fixx new root
        return item._key, item._value

# 8. Merging Two Heaps
# We are given two heaps and a key k
# We create a new heap with the root node storing k and with the two heaps as subtrees
# We perform downheap to restore the heap-order property

# 9. Bottom-up Heap Construction
# We can construct a heap storing n given keys in using a bottom-up construction with log n phases
# In phase i, pairs of heaps with 2^i -1 keys are merged into heaps with 2^(i+1) -1 keys

# Algorithms for Heap Construction


def __init__(self, contents=()):
    """Create a new priority queue.
    By default, queue will be empty. If contents is given, it should be as an iterable sequence of (k,v) tuples
    specifying initial condionts"""

    self._data = [self._item(k, v) for k, v in contents]    # empty by default
    if len(self._Data) > 1:
        self._heapify()

def _heapify(self):
    start = self._parent(len(self) - 1)         # start at PARENT of last leaf
    for j in range(start, -1, 1):               # going to and including the root
        self._downheap(j)

# Analysis of Heap Construction
# We visualize the worst-case time of a downheap with a proxy path that goes first right and then repeatedly goes left
#   until the bottom of the heap (this path may differ from the actual downheap path)
# Since each node is traversed by at most two proxy paths, the total number of nodes of the proxy paths is O(n)
# Thus, bottom-up heap construction runs in O(n) time
# Bottom-up heap construction is faster than n successive insertions and speeds up the first phase of heap-sort

import sys

# Maps and Hash Tables

# Maps
# A map is a searchable collection of items that are key-value pairs
# The main operations of a map are for searching, inserting, and deleting items
# Multiple items with the same key are not allowed
# Applications:
# - address book
# - student-record database

# Dictionaries
# Python's dict class is arguably the most significant data structure in the language
# - it represents an abstraction known as a dictionary in which unique keys are mapped to associated values
# Here, we use the term "dictionary" when specifically discussing Python's dict class, and the term "map" when
#   discussing the more general notion of the abstract data type

# The Map ADT (Using dict Syntax)
# M[k]: Return the value v associated with key k in map M, if one exists; otherwise, raise a Key Error
# In python, this is implemented with the special method __getitem__
# M[k] = v: Associate value v with key k in map M, replacing the existing value if the map already contains an item
# with key equal to k. In python, this is implemented with the special method __setitem__
# del M[k]: Remove from map M the item with key equal to k; if M has no such item, then raise a KeyError. In Python,
# this is implemented with the special method __delitem__
# len(M): Return the number of items in map M, In Python this is implemented with the special method __len__
# iter(M): The default iteration for a map generates a sequence of keys in the map. In Python, this is implemented
# with the special method __len__, and it allows loops of the form, for k in M
# k in M: Return True if the map contains an item with key k. In Python, this is implemented with the special
# __contains__ method
# M.get(k, d=None): Return M[k] if key k exists in the map; otherwise return default value d. This provides a form
# to query M[k] without risk of a KeyError
# M.setdefault(k, d): If key k exists in the map, simply return M[k]; if key k does not exist, set M[k] = d and
# return that value
# M.pop(k, d=None): Remove the item associated with key k from the map return its associated value v. If key k is not
# in the map, return default value d (or raise KeyError if parameter d is None).
# M.popitem(): Remove an arbitrary key-value pair from the map, and return a (k,v) tuple representing the removed pair.
# If map is empty, raise a KeyError
# M.clear(): Remove all key-value pairs from the map.
# M.keys(): Return a set-like view of all keys of M.
# M.values(): Return a set-like view of all values of M.
# M.items(): Return a set-like view of (k,v) tuples for all entries of M.
# M.update(M2): Assign M[k] = v for every (k,v) pair in map M2.
# M==M2: Return True if maps M and M2 have identical key-value associations
# M!=M2: Return True if maps M and M2 do not have identical key-value associations

# Learn from Examples
# Goal: Counting the number of occurrence s of words in a document
# Map is an idea structure:
# - Key: word
# - Value: word occurrences / frequency of the word
# Processing:
# _ lowercase all pieces of the document
# - omit all non-alphabetic characters (parentheses, apostrophes, punctuations)
from random import randrange

filename = sys.argv[1]

freq = {}
for piece in open(filename).read().lower().split():
    # only consider alphabetic characters within this piece
    word = ''.join(c for c in piece if c.isalpha())
    if word:
        freq[word] = 1 + freq.get(word, 0)
ma_word = ''
max_count = 0
for (w, c) in freq.items():     # (key, value) tuples represent (word, count)
    if c > max_count:
        max_word = w
        max_count = c
print('The most frequent word is', max_word)
print('Its number of occurrences is', max_count)

# Python Implementation
# The Python collections module provide an abstract base class for maps
from collections import MutableMapping
# Five core abstract methods that must be implemented by its subclass
# __getitem__, __setitem__, __delitem__, __len__, __iter__

# New Abstract BaseClass: MapBase
# Inherit from the class MutableMapping
# Provide a nested class: item, representing key-value pairs

class MapBase(MutableMapping):
    """Our own abstract base class that includes a nonpublic _Item class."""

    # Nested _Item class
    class _Item:
        """Lightweight composite to store key-value pairs as map items."""
        __slots__ = 'key', 'value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def eq(self, other):
            return self._key == other._key      # compare items based on their keys

        def __ne__(self, other):
            return not (self == other)          # opposite of __eq__

        def __lt__(self, other):
            return self._key < other._key       # compare items based on their keys

# List-Based Map
# We can efficiently implement a map using an unsorted map
# - we store the items of the map in a list S (based on a double-linked list), in arbitrary order
# An implementation of the Unsorted Map using Python list
# Every element of the list is an instance of the nested _Item class, providing a pair of key-valye
# Use a list .table to store all items
# Implement five core methods

# Unsorted List Implementation

class UnsortedTableMap(MapBase):
    """Map implementation using an unordered list."""

    def __init__(self):
        """Create an empty map."""
        self._table = []            # list of _Item's

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        for item in self._table:
            if k == item._key:
                return item._value
            raise KeyError('Key Error: ' | repr(k))

    def __setitem__(self, k, v):
        """Assign value v to k, overwriting existing value if present."""
        for item in self._table:
            if k == item._key:              # found a match
                item._value = v             # reassign value
                return                      # and quit
            # did not find match for key
            self._table.append(self._item(k, v))

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        for j in range(len(self._table)):
            if k == self._table[j]._key:
                self._table.pop(j)
                return
            raise KeyError('Key Error: ' | repr(k))

    def __len__(self):
        """Return number of items in the map."""
        return len(self._table)

    def __len__(self):
        """Generate iteration of the map's keys."""
        for item in self._table:
            yield item._key             # yield the KEY

# Performance of a List-Based Map
# Performance:
# - inserting an item takes O(1) time since we can insert the new item at the beginning or at the end of the sorted list
# - searching for or removing an item takes O(n) time, since the worst case (the item is not found) we traverse the
#   entire list to look for an item with the given key
# The unsorted list implementation is effective oly for maps of small size or for maps in which insertions are the most
# common operations, while searches and removals are rarely performed (e.g., historical record of logins to a
# workstation)

# Hash Tables
# Recall the notion of a Map
# - intuitively, a map M supports the abstraction of using keys as indices with a syntax such as M[k]
# - as a mental warm-up, consider a restricted setting in which a map with n items uses keys that are known to be
#   integers in a range from 0 to N-1, for some N >= n
# But what should we do if our keys are not integers in the range from 0 to N-1?
# - use a hash function to map general keys to corresponding indices in a table
# - for instance, the last four digits of a Social Security number

# Hash Functions and Hash Tables
# A hash function h maps keys of a given type to integers ina fixed interval [0, N-1]
# Example: h(x) = x mod N
#            -> is a hash function for integer keys
# The integer h(x) is called the hash value of key x
# A hash table for a given key type consists of
# - Hash function h
# - Array (called table) of size N
# When implementing a map with a hash table, the goal is to store item (k, o) at index i = h(k)

# SSN example:
# We design a hash table for a map storing entries as (SSN, Name), where SSN (social security number) is a nine-digit
# positive integer
# Our hash table uses an array of size N = 10,000 and the hash function h(x) = last four digits of x

# Hash Functions
# A hash function is usually specified as the composition of two functions:
# - Hash code:
#       h1: keys -> integers
# - Compression function:
#       h2: integers -> [0, N-1]
# The hash code is applied first, and the compression function is applied next on the result, i.e., h(x) = h2(h1(x))
# The goal of the hash function is to "disperse" the keys in apparently random way

# Hash Codes
# Memory Address:
# - We reinterpret the memory address of the key object as an integer Good in general, except for numeric and string
#   keys
# Integer cast:
# - We reinterpret the bits of the keys as an integer
# - Suitable for keys of length less than or equal to the number of bits of the integer
# Component sum:
# - We partition the bits of the key into components of fixed length (e.g., 16 or 32 bits) and we sum the components
#   (ignoring overflows)
# - Suitable for numeric keys of fixed length greater than or equal to the number of bits of the integer type
# Polynomial accumulation:
# - We partition the bits of the key into a sequence of components of fixed length ( e.f., 8, 16 or 32 bits)
#   a0a1...an-1
# - We evaluate the polynomial p(z) = a0 + a1z + a2z^2 + ... + an-1 z^(n-1) at a fixed value z, ignoring overflows
# - Especially suitable for strings (e.g., the choice z = 33 gives at most 6 collisions on a set of 50,000 English
#   words)
# Polynomial p(z) can be evaluated in O(n) time using Horner's rule:
# - the following polynomials are successively computed, each from the previous one in O(1) time
#       p0(z) = an-1
#       pi(z) = an-i-1 = z*pi-1(z)
#       (i = 1, 2, ..., n-1)
# We have p(z) = pn-1(z)

# Compression Functions
# Division:
# - h2(y) = y mod N
# - the size N of the hash table is usually chosen to be a prime
# - the reason has to do with number theory and is beyond the scope of this course
# Multiply, Add and Divide (MAD):
# - h2 (y) = (ay + b) mod N
# - a and b are non-negative integers such that: a mod N != 0
# - Otherwise, every integer would map to the same value b

# Abstract Hash Table Class


class HashMapBase(MapBase):
    """Abstract base class for map using hash-table with MAD compression."""

    def __init__(self, cap=11, p=109345121):
        """Create an empty hash-table map."""
        self._table = cap * [None]
        self._n = 0                         # number of entries in the map
        self._prime = p                     # prime for MAd compression
        self._scale = 1 + randrange(p-1)    # scale from 1 tp p-1 for MAD
        self._shift = randrange(p)          # shift from 0 to p-1 for MAD

    def _hash_function(self, k):
        return (hash(k)*self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)       # may raise KeyError

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)               # subroutine maintains elf._n
        if self._n > len(self._table) // 2:         # keep load factor <= 0.5
            self._resize(2*len(self._table) - 1)    # number 2*x -1 is often prime

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)              # may raise KeyError
        self._n -= 1

    def _resize(self, c):               # resize bucket array to capacity c
        old = list(self.items())        # use iteration to record existing items
        self._table = c * [None]        # then reset table to desired capacity
        self._n = 0                     # n recomputed during subsequent adds
        for (k, v) in old:
            self[k] = v                 # reinsert old key-value pair

# Collision Handling
# Collision occur when different elements are mapped to the same sell
# Separate chaining let each cell in the table point to a linked list of entries that map there
# Separate chaining is simple, but requires additional memory outside the table

# Map with Separate Chaining
# Delegate operations to a list-based map at each cell:
# Algorithm get(k):
# Return A[h(k)].get(k)

# Algorithm put(k,v)
# t = A[h(k)].put(k,v)
# if t = null then        {k is a new key}
#    n = n + 1
# return t

# Algorithm remove(k):
# t = A[h(k)].remove(k)
# if t != null then       {k was found}
#    n = n - 1
# return t

# Hash Table with Separate Chaining


class ChainHashMap(HashMapBase):
    """Hash map implemented with separate chaining for collision resolution."""

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error:' + repr(k))          # no match found
        return bucket[k]                                    # may raise KeyError

    def _bucket_setitem(self, j, k, v):
        if self._table [j] is None:
            self._table[j] = UnsortedTableMap()       # bucket is new to the table
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:             # key was new to the table
            self._n += 1                              # increase overall map size

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))         # no match found
        del bucket[k]                                       # may raise KeyError

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:                          # a nonempty slot
                for key in bucket:
                    yield key

# Linear Probing
# Open addressing: the colliding item is placed in a different cell of the table
# Linear probing: handles collisions by placing the colliding item in the next (circularly) available table cell
# Each table cell inspected is referred to as a “probe”
# Colliding items lump together, causing future collisions to cause alonger sequence of probes
# Example: h(x) = x mod 13
# – Insert keys 18, 41, 22, 44, 59, 32, 31, 73, in this order

# Search with Linear Probing
# Consider a hash table A that uses linear probing
# get(k)
# - we start at cell h(k)
# - we probe consecutive locations until one of the following occurs
#       - an item with key k is found, or
#       - an empty cell is found, or
#       - N cells have been unsuccessfully probed

# Algorithm get(k)
#   i  h(k)
#   p  0
#   repeat
#       c  A[i]
#       if c = 
#           return null
#       else if c.getKey () = k
#           return c.getValue()
#       else
#           i  (i + 1) mod N
#           p  p + 1
#  until   p = N
#  return null

# Updates with Linear Probing
# To handle insertions and deletions, we introduce a special object, called AVAILABLE, which replaces deleted elements
# remove(k)
# - we search for an entry with key k
# - if such an entry (k, o) is found, we place it with the special item AVAIABLE and we return element 0
# - else, we return null
# put(k, o)
# - we throw an exception if the table is full
# - we start at cell h(k)
# - we probe consecutive cells until one of the following occurs
#       a cell i is founf that is either empty or stores AVAILABLE or
#       N cells have been unsuccessfully probed
# - we store (k, o) in cell i

# Hash Table with Linear Probing


class ProbeHashMap(HashMapBase):
    """Hash map implemented with linear probing for collision resolution."""
    _AVAIL = object()       # sential marks locations of previous deletions

    def _is_available(self, j):
        """Return True if index j is available in table."""
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        """Search for key k in bucket at index j.
        Return (success, index) tuple, described as follows:
        If match was found, success is True and index denotes its location.
        If no match was found, success is False and index denotes first available slot."""

        firstAvail = None
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j                  # mark this as first avail
                if self._table[j] is None:
                    return (False, firstAvail)      # search has failed
                elif k == self._table[j]._key:
                    return True, j                  # found a match
                j = (j + 1) % len(self._table)      # keep looking (cyclically)

    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[s]._value

    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] = self._item(k,v)
            self._n += 1
        else:
            self._table[s]._value = v

    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        self._table[s] = ProbeHashMap._AVAIL

    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key

# Double Hashing
# Double hashing uses a secondary hash function d(k) and handles collisions by placing an item in the first available
# cell of the series (i + j * d(k)) mod N for j = 0, 1, ..., N-1
# The secondary hash function d(k) cannot have zero values
# The table size N must be a prime to allow probing of all the cells
# Common choice of compression function for the secondary hash function:
#   d2(k) = q - k mod q
#   where
#   q < N
#   q is a prime
# The possible values for d2(k) are 1, 2, ..., q

# Example of Double Hashing
# Consider a hash table storing integer keys that handles collision with double hashing
# - N = 13
# - h(k) = k mod 13
# - d(k) = 7 - k mod 7
# Insert keys 18, 41, 22, 44, 59, 32, 31, 73, in this order

# Performance of Hashing
# In the worst case, searches, insertions and removals on a hash table take O(n) time
# The worst case occurs when all the keys inserted into the map collide
# The load factor alpha n/N affects the performance of a hash table
# Assuming that the hash values are like random numbers, it can be shown that the expected number of probes for an
# insertion with open addressing is 1 / (1 - alpha)
# The expected running time of all the dictionary ADT operations in a hash table is O(1)
# In practice, hashing is very fast provided the load factor is not close to 100%
# Applications of hash tables:
# - small databases
# - compilers
# - browser caches

# Binary Search Trees

# Ordered Maps
# Keys are assumed to come from a total order
# Items are stored in order by their keys
# This allows us to support nearest neighbor queries:
# - items with largest key less than or equal to k
# - items with smallest key greater than or equal to k

# Binary Search
# Binary search can perform nearest neighbor queries on an ordered map that is implemented with an array, sorted by key
# - at each step, the number of candidate items is halved
# - terminates after O(log n) steps

# Search Tables
# A search table is an ordered map implemented by means of a sorted sequence
# - we store the items in an array-based sequence, sorted by key
# - we use an external comparator for the keys
# Performance:
# - searches take O(log n) time, using binary search
# - inserting a new item takes O(n) time, since in the worst case we have to shift n/2 items to make room for the new
#   item
# - removing an item takes O(n) time, since in the worst case we have to shift n/2 items to compact the items after the
#   removal
# The lookup table is effective only for ordered maps of small size or for maps on which searches are the most common
# operation, while insertions and removals are rarely performed (e.g., credit card authorizations)

# Sorted Map Operations
# Standard Map methods:
# - M[k]: return value v associated with key k in map M, if one exists; otherwise raise a KeyError; implemented
#   with __getitem__ method
# - M[k] = v: associate value v with key k in map M, replacing the existing value if the map already contains an item
#   with key equal to kl implemented with __setitem__ method
# - del M[k]: remove from map M the item with key equal to k; if M has no such item, then raise a KeyError; implemented
#   with __delitem__ method
# The sorted map ADT includes additional functionality, guaranteeing that an iteration reports keys in sorted order, and
# supporting additional searches such as find_gt(k) and find_range(start, stop)

# Binary Search Trees
# A binary search tree is a binary tree storing key values (or key-val
# .ue items) at its nodes and satisfying the
# following property:
# - let u, v, w be three nodes such that u is in the left subtree of v and w is in the right subtree of v. We have
#   key(u) <= key(v) <= key(w)
# External nodes do not store items, instead we consider them as None
# An inorder traversal of a binary tree visits the keys in increasing order
# Major ADT operators:
# - Search
# - Insertion
# - Deletion

# Search
# To search for a key k, we trace a downward pth starting at the root
# The next node visited depends on the comparison of k with the key of the current node
# If we reach a leaf, the key is not found
# Example: find(4)
# - Call TreeSearch(4, root)
# The algorithms for nearest neighbor queries are similar

# Algorithm TreeSearch(T, p, k)
#   if k == p.key then
#       return p                                                {successful search}
#   else if k < p.key() and T.left(p) is not None then
#       return TreeSearch(T, T.left(p), k)                      {recur on left subtree}
#   else if k > p.key() and T.right(p) is not None then
#       return TreeSearch(T, T.right(p), k)                     {recur on right subtree}
#   return p                                                    {successful search}

# Insertion
# To perform operation put(k, o), we search for key k (using TreeSearch)
# Assume k is not already in the tree, and let w be the (None) leaf reached by the search
# We insert k at node w and expand w into an internal node
# Example: insert 5

# Insertion Pseudo-code
# Algorithm TreeInsert(T, k, v)
#   input: A search key to be associated with value v
#   p = TreeSearch(T, T.root(), k)
#   if k == p.key() then
#       Set p's value to v
#   else if k < p.key() then
#       add node with item (k, v) as left child of p
#   else
#       add node with item (k, v) as right child of p

# Deletion
# To perform operation remove(k), we search for key k
# Assume key k is in the tree, and let v be the node storing k
# if node v has a (None) leaf child w, we remove v and w from the tree with opperation removeExternal(w), which removes
# w and its parent
# Example: remove 4
# We consider the case where the key k to be removed is stored at a node v whose children are both internal
# - we find the internal node w that follows v in an inorder traversal
# - we copy key(w) into node v
# - we remove node w and its left child z (which must be a leaf) by means of operation remove External(z)
# Example: remove 3

# Performance
# Consider an ordered map with n items implemented by means of a binary search tree of height h
# - the space used is O(n)
# - search and update methods take O(h) time
# The height h is O(n) in the worst case and O(log n) in the best case

from Lecture7 import LinkedBinaryTree
from Lecture9 import MapBase

class TreeMap(LinkedBinaryTree, MapBase):
    """Sorted map implementation using a binary search tree."""

    # override Position class
    class Position(LinkedBinaryTree.Position):
        def key(self):
            """Return key of map's key-value pair."""
            return self.element()._key

        def value(self):
            """Return value of map's key-value pair."""
            return self.element()._value

    # nonpublic utilities
    def _subtree_search(self, p, k):
        """Return Position of p's subtree having key k, or last node searched."""
        if k == p.key():                                            # found match
            return p
        elif k < p.key():                                           # search left subtree
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)
        else:                                                       # search right subtree
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)
        return p                                                    # unsuccessful search

    def _subtree_first_position(self, p):
        """Return Position of first item in subtree rooted at p."""
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self, p):
        """Return Position of last item in subtree rooted at p"""
        walk = p
        while self.right(walk) is not None:
            walk = self.right(walk)
        return walk

    def first(self):
        """Return the first Position in the tree (or None if empty)."""
        return self._subtree_first_position(self.root)

    def last(self):
        """Return last Position in the three (or None if empty)."""
        return self._subtree_last_position(self.root()) if len(self) > 0 else None

    def before(self, p):
        """Return the Position just before p in the natural order.
        Return None if p is the first position."""
        self._validate(p)       # inherited from LinkedBinaryTree
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            # walk upward
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above

    def after(self, p):
        """Return the Position just after p in the natural order.
        Return None if p is the last position."""
        self._validate(p)  # inherited from LinkedBinaryTree
        if self.right(p):
            return self._subtree_last_position(self.right(p))
        else:
            # walk upward
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above

    def find_position(self, k):
        """Return position with key k, or else neighbor (or None if empty)."""
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)           # hook for balanced tree subclass
            return p

    def find_min(self):
        """Return (key, value) pair with minimum key (or None if empty)."""
        if self.is_empty():
            return None
        else:
            p = self.first()
            return p.key(), p.value()

    def find_ge(self, k):
        """Return (key, value) pair with least key greater than or equal to k.
        Return None if there does not exist such a key."""
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if p.key() < k:                 # may not fund exact match
                p = self.after(p)           # p's key is too small
                return p.key(), p.value() if p is not None else None

    def find_range(self, start, stop):
        """Iterate all (key, value) pairs such that start <- key < stop.
        If start is None, iteration begins with minimum key of map.
        If stop is None, iteration continues through the maximum key of map."""
        if not self.is_empty():
            if start is None:
                p = self.first()
            else:
                # we initialize p with logic similar to find_ge
                p = self.find_position(start)
                if p.key() < start:
                    p = self.after(p)
                while p is not None and (stop is None or p.key() < stop):
                    yield p.key(), p.value()
                    p = self.after(p)

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        if self.is_empty():
            raise KeyError('KeyError: ' + repr(k))
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)           # hook for balanced tree subclasses
            if k != p.key():
                raise KeyError('Key Eroor: ' + repr(k))
            return p.value()

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        if self.is_empty():
            leaf = self._add_root(self._item(k, v))     # from LinkedBinaryTree
        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                p.element()._value = v                  # replace existing item's value
                self.__rebalance_access(p)              # hook for balanced tree subclasses
                return
            else:
                item = self._item(k, v)
                if p.key() < k:
                    leaf = self._add_right(p, item)     # inherited from LinkedBinaryTree
                else:
                    leaf = self._add_left(p, item)      # inherited from LinkedBinaryTree
        self._rebalance_insert(leaf)                    # hook for balanced tree subclasses

    def __iter__(self):
        """Generate an iteration of all keys in the map in order."""
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)

    def delete(self, p):
        """Remove the item at given Position."""
        self._validate(p)                       # inherited from LinkedBinaryTree
        if self.left(p) and self.right(p):      # p has two children
            replacement = self._subtree_last_position(self.left(p))
            self._replace(p, replacement.element())     # from LinkedBinaryTree
            p = replacement
            # now p has at most one child
        parent = self.parent(p)
        self._delete(p)                         # inherited from LinkedBinaryTree
        self._rebalance_delete(parent)          # if root deleted, parent is None

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if k == p.key:
                self.delete(p)              # rely on positional vision
                return                      # successful deletion complete
            self._rebalance_access(p)       # hook for balanced tree subclasses
        raise KeyError('KeyError: ' + repr(k))


# Search Tree Topics not covered
# Augmenting a standard binary search tree with occasional operations to reshape the tree and reduce its height
# Five methods
# - Balanced Search Trees
# - AVL Trees
# - Splay Trees
# - (2, 4) Trees
# - Red-Black Trees


# Sorting
# Sorting is among the most important, and well studied, of computing problems
# We already learned multiple sorting algorithms
# - Selection-sort
# - Insertion-sort
# - Heap-sort
# Python class list: .sort() or .sorted()

# Algorithm: Merge-Sort
# Divide-and-conquer is a general algorithm design paradigm:
# - divide: divide the input data S into two disjoint subsets S1 and S2
# - recur: solve the subproblems associated with S1 and S2
# - conquer: combine the solutions for S1 and S2 into a solution for S
# The best case for the recursion are subproblems of size 0 or 1
# Merge-sort is a sorting algorithm based on the divide-and-conquer paradigm
# Like heap-sort
# - it has O(n log n) running time
# Unlike heapsort
# - it does not use an auxiliary priority queue
# - it accesses data in a sequential manner (suitable to sort data on a disk)

# Merge-Sort
# Merge-sort on an input sequence S with n elements consists of three steps:
# - divide: partition S into two sequences S1 and S2 of about n/2 elements each
# - recur: recursively sort S1 and S2
# - conquer: merge S1 and S2 into a unique sorted sequence

# Algorithm mergeSort(S)
#   Input sequence S with n elements
#   Output sequence S sorted according to C
#   if S.size > 1
#       (S1, S2) <- partition(S, n/2)
#       mergeSort(S1)
#       mergeSort(S2)
#       S <- merge(S1,S2)

# Merging Two Sorted Sequences
# The conquer step of merge-sort consists of merging two sorted sequences A and B into a sorted sequence S containing
# the union of the elements of A and B
# Merging two sorted sequences, each with n/2 elements and implemented by means of a doubly linked list takes O(n) time

# Algorithm merge(A, B)
#   Input sequences A and B with n/2 elements each
#   Output sorted sequence of A union B
#   S <- empty sequence
#   while ! A.isEmpty() and ! B.isEmpty()
#       if A.first().element() < B.first().element()
#           S.addLast(A.remove(A.first()))
#       else
#           S.addLast(B.remove(B.first()))
#   while ! A.isEmpty()
#       S.addLast(A.remove(A.first()))
#   while ! B.isEmpty()
#       S.addLast(B.remove(B.first()))
#   return S


def merge(S1, S2, S):
    """Merge two sorted Python lists S1 and S2 into properly sized list S."""
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i<len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i]      # copy ith element of S1 as next item of S
            i += 1
        else:
            S[i+j] = S2[j]      # copy jth element of S2 as next item of S
            j += 1

def merge_sort(S):
    """Sort the elements of Python list S using the merge-sort algorithm."""
    n = len(S)
    if n < 2:
        return                  # list is already sorted
    # divide
    mid = n // 2
    S1 = S[0:mid]               # copy of first half
    S2 = S[mid:n]               # copy of second half
    # conquer (with recursion)
    merge_sort(S1)              # sort copy of first half
    merge_sort(S2)              # sort copy of second half
    # merge results
    merge(S1, S2, S)            # merge sorted halves back into S

# Merge-Sort Tree
# An execution of merge-sort is depicted by a binary tree
# - each node represents a recursive call of merge-sort and stores
#       unsorted sequence before the execution and its partition
#       sorted sequence at the end of the execution
# - the root is the initial call
# - the leaves are calls on subsequences of size 0 or 1

# Analysis of Merge-Sort
# The height h of the merge-sort tree is O(log n)
# - at each recursive call we divide in half the sequence
# The overall amount of work done at the nodes of depth i is O(n)
# - we partition and merge 2^i sequences of size n/2^i
# - we make 2^i+1 recursive calls
# Thus, the total running time of merge-sort is O(n log n)

# Summary of Sorting Algorithms
# Selection-sort - O(n^2)
# - slow
# - in-place
# - for small data sets (<1k)
# Insertion-sort - O(n^2)
# - slow
# - in-place
# - for small data sets (<1k)
# Heap-sort - O(n log n)
# - fast
# - in-place
# - for large data sets (!k - 1m)
# Merge-sort - O(n log n)
# - fast
# - sequential data access
# - for huge data sets (>1m)

# Algorithm: Quick-Sort
# Quick-sort is a randomized sorting algorithm based on the divide-and-conquer paradigm:
# Divide: pick a random element x (called pivot) and partition S into:
# - L elements less than x
# - E elements equal to x
# - G elements greater than x
# Recur: sort L and G
# Conquer: join L, E, and G

# Partition
# We partition an input sequence as follows
# - we remove, in turn, each element y from S and
# - we insert y into L, E, or G depending on the result of the comparison with the pivot x
# Each insertion and removal is at the beginning or at the end of a sequence, and hence takes O(1) time
# Thus, the partition step of quick-sort takes O(n) time

# Algorithm partition(S,p)
#   Input: sequence S, position p of pivot
#   Output: subsequences, L, E, G of the elements of S less than, equal to, greater than the pivot
#   L,E,G <- empty sequences
#   x <- S.remove(p)
#   while ! S.isEmpty()
#       y <- S.remove(S.first())
#       if y < x
#           L.addLast(y)
#       else if y = x
#           E.addLast(y)
#       else    {y > x}
#           G.addLast(y)

from Lecture6 import LinkedQueue

def quick_sort(S):
    """Sort the elements of queue S using the quick-sort algorithm."""
    n = len(S)
    if n < 2:
        return                           # list is already sorted
    # divide
    p = S.first()                        # using first as arbitrary pivot
    L = LinkedQueue()
    E = LinkedQueue()
    G = LinkedQueue()
    while not S.is_empty():              # divide S into L, E, and G
        if S.first() < p:
            L.enqueue(S.dequeue())
        elif p < S.first():
            G.enqueue(S.dequeue())
        else:                            # S.first() must equal pivot
            E.enqueue(S.dequeue())
    # conquer (with recursion)
    quick_sort(L)                        # sort elements less than p
    quick_sort(G)                        # sort elements greater than p
    # concatenate results
    while not L.is_empty():
        S.enqueue(L.dequeue())
    while not E.is_empty():
        S.enqueue(E.dequeue())
    while not G.is_empty():
        S.enqueue(G.dequeue())

# Worse-case Running Time
# THe worst case for quick-sort occurs when the pivot is the unique minimum or maximum element
# One of L and G has size n-1 and the other has size 0
# The running time is proportional to the sum n + (n-1) + ... + 2 + 1
# Thus, the worst-case running time of quick-sort is O(n^2)

# Quick-Sort Tree
# An execution of quick-sort is depicted by a binary tree
# - each node represents a recursive call of quick-sort and stores
#       unsorted sequence before the execution and its pivot
#       sorted sequence at the end of the execution
# - the root is the initial call
# - the leaves are calls on subsequences of size 0 or 1

# Expected Running Time
# Consider a recursive call of quick-sort on a sequence of size s
# - Good call: the sizes of L and G are each less than 3s/4
# - Bad call: one of the L and G has size greater than 3s/4
# A call is good with probability 1/2
# - 1/2 of the possible pivots cause good calls
# Probabilistic fact: The expected number of coin tosses required in order to get k heads is 2k
# For a node of depth i, we expect
# - i/2 ancestors are good calls
# - the size of the input sequence for the current call is at most (3/4)^(i/2) * n
# Therefore, we have
# - for node of depth 2 log (4/3) N, the expected input size is one
# - the expected height of the quick-sort tree is O(log n)
# The amount of work done at the nodes of the same depth is O(n)
# Thus, the expected running time of quick-sort is O(n log n)

# In-Place Quick-sort
# Quick-sort can be implemented to run in place
# In the partition stepm we use replace operations to rearrange the elements of the input sequence such that
# - the elements less than the pivot have rank less than h
# - the elements equal to the pivot have rank between h and k
# - the elements greater than the pivot have rank greater than k
# The recursive calls consider
# - elements with rank less than h
# - elements with rank greater than k

# Algorithm inPlaceQuickSort(S,l,r)
#   input sequence S, ranks l and r
#   output sequence S with the elements of rank between l and r rearranged in increasing order
#   if l >= r
#       return
#   i <- a random integer between l and r
#   x <- S.elemAtRank(i)
#   (h,k) <- inPlacePartition(x)
#   inPlaceQuickSort(s,l,h-1)
#   inPlaceQuickSort(S,k+1,r)

# In-Place Partitioning
# Perform the partition using two indices to split S into L and E U G (a similar method can split E U G into E and G)
# Repeat until j and k cross:
# - scan j to the right until finding an element >= x
# - scan k to the left until finding an element < x
# - swap elements at indices j and k

# Python implementation:

def inplace_quick_sort(S, a, b):
    """Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm."""
    if a >= b:
        return                              # range is trivially sorted
    pivot = S[b]                            # last element of range is pivot
    left = a                                # will scan rightward
    right = b - 1                           # will scan leftward
    while left <= right:
        # scan until reaching value equal or larger than pivot (or right marker)
        while left <= right and S[left] < pivot:
            left += 1
        # scan until reaching value equal or smaller than pivot (or left marker)
        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right:                             # scans did not strictly cross
            S[left], S[right] = S[right], S[left]     # swap values
            left, right = left + 1, right - 1         # shrink range
    # put pivot into its final place (currently marked by left index)
    S[left], S[b] = S[b], S[left]
    # make recursive calls
    inplace_quick_sort(S, a, left - 1)
    inplace_quick_sort(S, left + 1, b)

# Summary of Sorting Algorithms
# Selection-sort - O(n^2)
# - in-place
# - slow (good for small inputs)
# Insertion-sort - O(n^2)
# - in-place
# - slow (good for small inputs)
# Quick-sort - O(n log n) expected
# - in-place, randomized
# - fastest (good for large inputs)
# Heap-sort - O(n log n)
# - in-place
# - fast (for large inputs)
# Merge-sort - O(n log n)
# - sequential data access
# - fast (good for huge inputs)

# Algorithm: Lens and Comparisons
# Comparison-Based Sorting
# Many sorting algorithms are comparison based
# - they sort by making comparisons
# - examples: bubble-sort, selection-sort, insertion-sort, heap-sort, merge-sort, quick-sort,...
# Let us therefore derive a lower bound on the running time of any algorithm that uses comparisons to sort n elements,
# x1, x2,..., Xn

# Counting Comparisons
# Let us just count comparisons then
# Each possible run of the algorithm corresponds to a root-to-leaf path in a decision tree

# Decision Tree Height
# The height of the decision tree is a lower bound on the running time
# Every input permutation must lead to a separate leaf output
# Since there are n!= 1*2*...*n leaves, the height is at least log (n!)

# The Lower Bound
# Any comparison-based sorting algorithms takes at least log(n!) time
# Therefore, any such algorithm takes time at least:
#       log(n!) >= log(n/2)^(n/2) = (n/2) log (n/2)
# That is, any comparison-based sorting algorithm must run in Omega(n log n) time

# Algorithm: Selection
# The selection problem:
# Given an integer k and n elements x1, x2, ..., xn, taken from a total order, find the kth smallest element in this set
# of course, we can sort the set in O(n log n) time and then index the k-th element
# --- Can we solve the selection problem faster? ---

# Quick-Select
# Quick-select is a randomized selection algorithm based on the prune-and-search paradigm:
#   - prune: pick a random element x (called pivot) and partition S into
#       L: elements less than x
#       E: elements equal x
#       G: elements greater than x
#   - search: depending on k, either answer is in E, or we need to recur in either L or G

# Partition
# We partition an input sequence as in the quick-sort algorithm:
# - we remove, in turn, each element y from S and
# - we insert y into L, E or G depending on the result of the comparison with the pivot x
# Each insertion and removal is at the beginning or at the end of a sequence, and hence takes O(1) time
# Thus, the partition step of quick-select takes O(n) time

# Algorithm partition(S,p)
#   input sequence S, position p of pivot
#   output subsequences L, E, G of the elements of S less than, equal to, or greater than the pivot
#   L, E, G <- empty sequences
#   x <- S.remove(p)
#   while not S.isEmpty()
#       y <- S.remove(S.first())
#       if y < x
#           L.addLast(y)
#       else if y = x
#           E.addLast(y)
#       else    {y > x}
#           G.addLast(y)
#  return L, E, G

# Quick-select Visualization
# An execution of quick-select can be visualized by a recursion path
# - each node represents a recursive call of quick-select, and stores k and the remaining sequence

# Expected Running TIme
# Consider a recursive call of quick-select on a sequence of size s
# - Good call: the sizes of L and G are each less than 3s/4
# - Bad call: one of L and G has size greater than 3s/4
# A call is good with probability 1/2
# - 1/2 of the possible pivots cause good calls
# Probabilistic Fact #1: The expected number of coin tosses required in order to get one head is two
# Probabilistic Fact #2: Expectation is a linear function:
#   - E(X+Y) = E(X) + E(Y)
#   - E(cX) = cE(X)
# Let T(n) denote the expected running time of quick-select
# By fact #2,
# - T(n) <= T(3n/4) + bn*(expected # of calls before a godo call)
# By fact #1,
# - T(n) <= T(3n/4) + 2bn
# That is, T(n) is a geometric series:
# - T(n) <= 2bn + 2b(3/4)n + 2b(3/4)^2 n + 2b(3/4)^3 n + ...
# So T(n) is O(n)
# We can solve the selection problem in O(n) expected time

# Bucket-Sort
# Let S be a sequence of n (key, element) items with keys in the range [0. N-1]
# Bucket-sort uses the keys as indices into an auxiliary array B of sequences (buckets)
#   Phase 1: Empty sequence S by moving each entry (k, o) into its bucket B[k]
#   Phase 2: for i = 0, ..., N-1, move the entries of bucket B[i] to the end of sequence S
# Analysis:
# - Phase 1 takes O(n) time
# - Phase 2 takes O(n+N) time
# Bucket-sort takes O(n+N) time

# Algorithm bucketSort(S):
# Input: sequence S of entries with integer keys in the range [0, N-1]
# Output: sequence S sorted in non-decreasing order of the keys
# Let B be an array of N sequences, each of which is initially empty
# for each entry e in S do
#   k = the key of e
#   remove e from S
#   insert e at the end of bucket B[k]
# for i = 0 to N-1 do
#   for each entry e in B[i] do
#       remove e from B[i]
#       insert e at the end of S

# Properties and Extensions
# Key-type Property
# - the keys are used as indices into an array and cannot be arbitrary objects
# - no external comparator
# Stable Sort Property
# - the relative order of any two items with the same key is preserved after the execution of the algorithm
# Extensions
# - integer keys in the range [a,b]
#       put entry (k,o) into bucket B[k-a]
# - String keys from a set D of possible strings, where D has constant size (e.g., names of the 50 US states)
#       Sort D and compute the rank r(k) of each string k of D in the sorted sequence
#       Put entry (k,o) into bucket B[r(k)]

# Lexicographic Order
# A d-tuple is a sequence of d keys (k1, k2, ..., kd) where key ki is said to be the i-th dimension of the tuple
# Example
# - the cartesian coordinates of a point in space are a 3-tuple
# The lexicographic order of two d-tuples is recursively defined as follows
#   (x1, x2, ..., xd) < (y1, y2, ..., yd) <=> x1<y1 V x1=y1 ^ (x2,..., xd) < (y2, ..., yd)
#   i.e., the tuples are compared by the first dimension then by the second dimension, etc.
# Let Ci be the comparator that compares two tuples by their i-th dimension
# Let stableSort(S,C) be a stable sorting algorithm that uses comparator C
# Lexicographic-sort sorts a sequence of d-tuples in lexicographic order by executing d times algorithm stableSort, one
# per dimension
# Lexicographic-sort runs in O(dT(n)) time, where T(n) is the running time of stableSort

# Algorithm lexicographicSort(S)
#   Input sequence S of d-tuples
#   Output sequence S sorted in lexicographic order
#   for i <- d down to 1
#       stableSort(S, Ci)

# Radix-Sort
# Radix-sort us a specialization of lexicographic-sort that uses bucket-sort as the stable sorting algorithm in each
# dimension
# Radix-sort is applicable to tuples where the keys in each dimension i are integers in the range [0, N-1]
# Radix-sort runs in time O(d(n+N))

# Algorithm radixSort(S<N)
#   Input: sequence S of d-tuples such that (O,...,0) <= (x1,...,xd( and (x1,...,xd) <=(N-1,...,N-1) for each tuple
#   (x1,...,xd) in S
#   Output: sequence S sorted in lexicographic order
#   for i <- d down to 1
#       bucketSort(S,N)

# Radix-sort for Binary Numbers
# Consider a sequence of n b-bit integers x = x_b-1... x_1x_0
# We represent each element asa b-tuple of integers in the range [0,1] and apply radix sort with N=2
# This application of radix-sort algorithm runs in O(bn) time
# For example, we can sort a sequence of 32-bit integers in linear time

# Algorithm binaryRadixSort(S)
# Input: sequence S of b-bit integers
# Output: sequence S sorted
# replace each element x of S with the item (0, x)
# for i<- 0 to b-1
#   replace the key k of each item (k,x) of S with bit xi of x
#   bucketSort(S,2)

