
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






























































