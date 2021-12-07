from .binary_tree import BinaryTree
from .linked_binary_tree import LinkedBinaryTree

# 4


class ArrayBinaryTree(BinaryTree):
    """ Implementing of binary tree by level numbering."""

    # nested class
    class Position(BinaryTree.Position):
        """ A class representing the location of a single element."""

        def __init__(self, container, index):
            """ Constructor should not be invoked by user."""
            self._container = container
            self._index = index

        def element(self):
            """ Return the element stored at this Position."""
            return self._container._data[self._index]

        def __eq__(self, other):
            """ Return Ture if other is a Position representing the same
            location."""
            return type(other) is type(self) and other._index == self._index

        def __hash__(self):
            """ Return hash code of this Position."""
            return hash(self._index)

    # utility methods
    def _validate(self, p):
        """ Return associated index, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p.element() is None:  # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._index

    def _make_position(self, index):
        """ Return Position instance for given node (or None if no node)."""
        if 0 <= index < len(self._data) and self._data[index] is not None:
            return self.Position(self, index)
        else:
            return None

    def _fill_data(self, idx):
        """ Full self._data to index `idx` with None."""
        while idx >= len(self._data):
            self._data.append(None)

    # public accessors
    def __init__(self):
        self._data = []
        self._size = 0

    def root(self):
        """ Return the root of tree, None if tree is empty."""
        return self._make_position(0)

    def parent(p):
        """ Return the Position of p's parent (or None if p is root)."""
        index = self._validate(p)
        if index % 2 == 0:
            return self._make_position((index-2)/2)
        else:
            return self._make_position((index-1)/2)

    def left(self, p):
        """ Return the Position of p's left child (or None if no left child).
        """
        index = self._validate(p)
        return self._make_position(2*index+1)

    def right(self, p):
        """ Return the Position of p's right child (or None if no right
        child)."""
        index = self._validate(p)
        return self._make_position(2*index+2)

    def num_children(self, p):
        """ Return the number of children of Position p."""
        count = 0
        if self.left(p) is not None:
            count += 1
        if self.right(p) is not None:
            count += 1
        return count

    def __len__(self):
        """ Return the total number of elements in the tree."""
        return self._size

    def __str__(self):
        """ String representation of linked binary tree."""
        s = ''
        for item in self:
            s += str(item)
        return s

    # nonpublic mutators
    def _add_root(self, e):
        """ Place element e at the root of an empty tree and return new
        Position.

        Raise ValueError if tree nonempty.
        """
        if len(self._data) > 0 and self._data[0] is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._data.append(e)
        return self._make_position(0)

    def _add_left(self, p, e):
        """ Create a new left child for Position p, storing element e.

        :return : the Position of new node
        :raise : ValueError if Position p is invalid or p already has a left
        child.
        """
        index = self.left(p)
        if index is not None:
            raise ValueError('Left child exists')
        self._size += 1
        left_idx = 2 * p._index + 1
        self._fill_data(left_idx)
        self._data[left_idx] = e
        return self._make_position(left_idx)

    def _add_right(self, p, e):
        """ Create a new right child for Position p, storing element e.

        :return : the Position of new node
        :raise : ValueError if Position p is invalid or p already has a right
        child.
        """
        index = self.right(p)
        if index is not None:
            raise ValueError('Right child exists')
        self._size += 1
        right_idx = 2 * p._index + 2
        self._fill_data(right_idx)
        self._data[right_idx] = e
        return self._make_position(right_idx)

    def _replace(self, p, e):
        """ Replace the element at position p with e, and return old element."""
        index = self._validate(p)
        if index is not None:
            old = self._data[index]
            self._data[index] = e
            return old

    def __recursive_move_forward(self, p):
        """ Move all the elements of subtree rooted at p forward in the data
        list. Forward means moving to their parent index."""
        if p is None:
            return
        index = self._validate(p)
        if index % 2 == 0:
            pidx = (index - 2) / 2
        else:
            pidx = (index - 1) / 2
        self._data[pidx] = self._data[index]
        self._data[index] = None
        lp = self._make_position(index * 2 + 1)
        rp = self._make_position(index * 2 + 2)
        self.__recursive_move_forward(lp)
        self.__recursive_move_forward(rp)

    def _delete(self, p):
        """ Delete the node at Position p, and replace it with its child, if
        any.

        :return : the element that had been stored at Position p.
        :raise : ValueError if Position p is invalid or p has two children.
        """
        index = self._validate(p)
        if index is None:
            raise ValueError('Invalid Position p')
        if self.num_children(p) == 2:
            raise ValueError('Position has two children')

        if self.left(p) is not None:
            child = self.left(p)
        else:
            child = self.right(p)

        self._size -= 1
        if child is not None:
            self.__recursive_move_forward(child)
        else:
            self._data[index] = None
        return

    def __recursive_copy_tree(self, srp, t, tp, left=True):
        """ Copy the tree elements to self recursively."""
        if tp is None:
            return
        else:
            index = t._validate(tp)
            flag = True if index == 0 and left else False
            if (not flag) and index % 2 == 0:
                idx = srp._index * 2 + 2
                self._fill_data(idx)
                self._data[idx] = t._data[index]
            else:
                idx = srp._index * 2 + 1
                self._fill_data(idx)
                self._data[idx] = t._data[index]
            sp = self._make_position(idx)
            self.__recursive_copy_tree(sp, t, t.left(tp))
            self.__recursive_copy_tree(sp, t, t.right(tp))

    def _attach(self, p, t1, t2):
        """ Attach trees t1 and t2, respectively, as the left and right
        subtrees of the external Position p. As a side effect, set t1 ans t2 to
        empty.

        :raise : TypeError if trees t1 and t2 do not match type of this tree.
        :raise : ValueError if Position p is invalid or not external.
        """
        index = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')

        self._size += len(t1) + len(t2)
        # attach t1
        self.__recursive_copy_tree(p, t1, t1.root())
        t1._data = []
        t1._size = 0
        # attach t1
        self.__recursive_copy_tree(p, t2, t2.root(), left=False)
        t2._data = []
        t2._size = 0


# 5


class ExpressionTreeV2(LinkedBinaryTree):
  """An arithmetic expression tree."""

  def __init__(self, token, left=None, right=None):
    """Create an expression tree.

    In a single parameter form, token should be a leaf value (e.g., '42'),
    and the expression tree will have that value at an isolated node.

    In a three-parameter version, token should be an operator,
    and left and right should be existing ExpressionTree instances
    that become the operands for the binary operator.
    """
    super().__init__()                        # LinkedBinaryTree initialization
    if not isinstance(token, str):
      raise TypeError('Token must be a string')
    self._add_root(token)                     # use inherited, nonpublic method
    if left is not None:                      # presumably three-parameter form
      if token not in '+-*x/':
        raise ValueError('token must be valid operator')
      self._attach(self.root(), left, right)  # use inherited, nonpublic method

  def __str__(self):
    """Return string representation of the expression."""
    pieces = []                 # sequence of piecewise strings to compose
    self._parenthesize_recur(self.root(), pieces)
    return ''.join(pieces)

  def _parenthesize_recur(self, p, result):
    """Append piecewise representation of p's subtree to resulting list."""
    if self.is_leaf(p):
      result.append(str(p.element()))                    # leaf value as a string
    else:
      result.append('(')                                 # opening parenthesis
      self._parenthesize_recur(self.left(p), result)     # left subtree
      result.append(p.element())                         # operator
      self._parenthesize_recur(self.right(p), result)    # right subtree
      result.append(')')                                 # closing parenthesis

  def evaluate(self):
    """Return the numeric result of the expression."""
    return self._evaluate_recur(self.root())

  def _evaluate_recur(self, p):
    """Return the numeric result of subtree rooted at p."""
    if self.is_leaf(p):
      return float(p.element())      # we assume element is numeric
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
      else:                          # treat 'x' or '*' as multiplication
        return left_val * right_val


def tokenize(raw):
  """Produces list of tokens indicated by a raw expression string.

  For example the string '(43-(3*10))' results in the list
  ['(', '43', '-', '(', '3', '*', '10', ')', ')']
  """
  SYMBOLS = set('+-x*/() ')    # allow for '*' or 'x' for multiplication

  mark = 0
  tokens = []
  n = len(raw)
  for j in range(n):
    if raw[j] in SYMBOLS:
      if mark != j:
        tokens.append(raw[mark:j])  # complete preceding token
      if raw[j] != ' ':
        tokens.append(raw[j])       # include this token
      mark = j+1                    # update mark to being at next index
  if mark != n:
    tokens.append(raw[mark:n])      # complete preceding token
  return tokens

def build_expression_tree(tokens):
  """Returns an ExpressionTree based upon by a tokenized expression.

  tokens must be an iterable of strings representing a fully parenthesized
  binary expression, such as ['(', '43', '-', '(', '3', '*', '10', ')', ')']
  """
  S = []                                        # we use Python list as stack
  for t in tokens:
    if t in '+-x*/':                            # t is an operator symbol
      S.append(t)                               # push the operator symbol
    elif t not in '()':                         # consider t to be a literal
      S.append(ExpressionTreeV2(t))               # push trivial tree storing value
    elif t == ')':       # compose a new tree from three constituent parts
      right = S.pop()                           # right subtree as per LIFO
      op = S.pop()                              # operator symbol
      left = S.pop()                            # left subtree
      S.append(ExpressionTreeV2(op, left, right)) # repush tree
    # we ignore a left parenthesis
  return S.pop()

if __name__ == '__main__':
  big = build_expression_tree(tokenize('(((5+3)x5)-((10*4)/2))'))
  print(big, '=', big.evaluate())
