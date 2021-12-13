
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


