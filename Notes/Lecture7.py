
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


