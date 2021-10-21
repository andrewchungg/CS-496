import random as r


# Question 2


def func(n):
    sum = 0
    n0 = n * n
    rows, cols = (n, n)
    a = []
    b = [[0] * cols] * rows
    for i in range (cols):
        col = []
        for j in range (rows):
            col.append(r.randint(0, 255))
        a.append(cols)
    print(a)
    for i in range(len(a)):
        for j in range(len(a[i])):
            sum = sum + a[i][j]
    mean = sum / n0
    print(mean)
    b = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
    print(b)
    for i in range(len(b)):
        for j in range(len(b[i])):
            b[i][j] = b[i][j] - mean
    print(b)


# Question 4


class _Node:
    def __init__(self, element, next=None):
        self._element = element
        self._next = next


class SLL:
    def __init__(self):
        self._head = None
        self._size = 0

    def insert(self, element):
        if self._head is None:
            self._head = _Node(element)
            self._size += 1
        else:
            temp = _Node(element)
            current = self._head
            while current._next is not None:
                current = current._next
            current._next = temp
            self._size += 1

    def length(self):
        return self._size

    def max(self):
        maximum = 0
        current = self._head
        while current is not None:
            if current._element > m:
                maximum = current._element
            current = current._next
        return maximum


# Question 5


def merge(linkedList1, linkedList2):
    newLinkedList = SLL()
    current1 = linkedList1._head
    current2 = linkedList2._head
    while current1 is not None and current2 is not None:
        if (current1._element <= current2._element):
            newLinkedList.insert(current1._element)
            current1 = current1._next
        else:
            newLinkedList.insert(current2._element)
            current2 = current2._next
    while current1 is not None:
        newLinkedList.insert(current1._element)
        current1 = current1._next
    while current2 is not None:
        newLinkedList.insert(current2._element)
        current2 = current2._next
    return newLinkedList


linkedList1 = SLL()
linkedList1.insert(1)
linkedList1.insert(3)
linkedList1.insert(5)

linkedList2 = SLL()
linkedList2.insert(2)
linkedList2.insert(4)
linkedList2.insert(6)

newLinkedList = merge(linkedList1, linkedList2)

print("The elements in the merged linked list are:")
current = newLinkedList._head
while current is not None:
    print(current._element)
    current = current._next

















