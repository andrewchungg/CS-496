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








