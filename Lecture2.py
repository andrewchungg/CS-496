
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




