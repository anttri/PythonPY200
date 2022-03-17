from collections import abc
from typing import Any, Optional

from node import Node

class LinkedList(abc.MutableSequence):

    def __init__(self):
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None

    def __getitem__(self, index):
        if index >= 0:
            current = self._head
            while current is not None:
                if index == 0:
                    return current
                index -= 1
                current = current._next
        raise IndexError("invalid index")

    def __setitem__(self, key, value):
        self[key].value = value

    def __delitem__(self, key):
        if (key == 0):
            self._head = self._head._next
        else:
            prev = self._head
            current = self._head
            while current is not None:
                if (key == 0):
                    break
                key -= 1
                prev = current
                current = current._next
            if (current):
                prev._next = current._next
                if (current == self._tail):
                    self._tail = prev

    def __len__(self):
        l = 0
        if self._head is None:
            return l
        else:
            current = self._head
            while current is not None:
                l += 1
                current = current._next
            return l

    def __str__(self):
        current = self._head
        j = ''
        while current is not None:
            j += str(current) + " "
            current = current._next
        return j

    def __repr__(self):
        return "[{}]".format(", ".join(map(str, self)))

    def insert(self, index, value):
        if index >= len(self):
            self.append(value)
        else:
            new_node = Node(value)
            if (index == 0):
                new_node._next = self._head
                self._head = new_node
            else:
                prev = self._head
                current = self._head
                while current is not None:
                    if (index == 0):
                        break
                    index -= 1
                    prev = current
                    current = current._next
                if (current):
                    prev._next = new_node
                    new_node._next = current

    def append(self, value):
        new_node = Node(value)
        if (self._head):
            self._tail._next = new_node
            self._tail = new_node
        else:
            self._head = self._tail = new_node

    def __iter__(self):
        current = self._head
        while current is not None:
            yield current.value
            current = current._next

    def __contains__(self, value):
        for val in self:
            if (val == value):
                return True
        return False

    def count(self, value):
        return sum(1 for val in self if val == value)

    def pop(self, i):
        val = self[i].value
        del self[i]
        return val

    def extend(self, other):
        for val in other:
            self.append(val)

    def remove(self, value):
        i = self.index(value)
        del self[i]

    def index(self, value):
        current = self._head
        i = 0
        while current is not None:
            if (current.value == value):
                return i
            i += 1
            current = current._next
        raise ValueError("invalid value")

class DoubleLinkedList(LinkedList):

    def __init__(self):
        LinkedList.__init__(self)

    def __delitem__(self, key):
        current = self[key]
        if (self._head == current):
            self._head = self._head._next
            if (self._head):
                self._head._prev = None
        elif (self._tail == current):
            self._tail = self._tail._prev
            if (self._tail):
                self._tail._next = None
        else:
            current._prev._next = current._next
            current._next._prev = current._prev

    def insert(self, index, value):
        if index >= len(self):
            self.append(value)
        else:
            current = self[index]
            prev = current._prev
            new_node = Node(value, _next=current, _prev=prev)
            if (prev):
                prev._next = new_node
            else:
                self._head = new_node
            current._prev = new_node

    def append(self, value):
        if (self._head):
            new_node = Node(value, _prev=self._tail)
            self._tail._next = new_node
            self._tail = new_node
        else:
            self._head = self._tail = Node(value)

    def __reversed__(self):
        current = self._tail
        while current is not None:
            yield current.value
            current = current._prev


if __name__ == "__main__":
    lst = LinkedList()
    lst.insert(100,1)
    lst.insert(0,2)
    lst.insert(1,3)
    assert lst[0].value == 2
    assert lst[1].value == 3
    assert lst[2].value == 1
    print(lst)



