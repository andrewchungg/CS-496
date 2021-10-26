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
