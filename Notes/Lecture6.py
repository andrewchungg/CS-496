
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