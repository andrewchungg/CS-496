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




