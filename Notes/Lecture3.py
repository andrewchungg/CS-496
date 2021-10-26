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








