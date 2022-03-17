class Node:
    def __init__(self, v):
        self.value = v
        self._next = None

    def get_next(self):
        return self._next

    def set_next(self, next):
        self._next = next

    def __str__(self):
        n = str(self.value)
        if (self.get_next()):
            n += " next to " + str(self.get_next().value)
        else:
            n += " next is null"
        return n

    def __repr__(self):
        return "Node(" + str(self.value) + ")"

    def is_valid(self):
        return True


class DoubleLinkedNode(Node):

    def __init__(self, v):
        super().__init__(v)
        self._prev = None

    def __str__(self):
        p = super().__str__()
        if (self.get_prev()):
            p += " prev to " + str(self.get_prev().value)
        else:
            p += " prev is null"
        return p

    def __repr__(self):
        return "DoubleLinkedNode(" + str(self.value) + ")"

    def get_prev(self):
        return self._prev

    def set_next(self, next):
        if (self._next):
            self._next._prev = None
        self._next = next
        if (next):
            next._prev = self

    def set_prev(self, prev):
        if (self._prev):
            self._prev._next = None
        self._prev = prev
        if (prev):
            prev._next = self


if __name__ == "__main__":
    ll_1 = DoubleLinkedNode(5)
    ll_2 = DoubleLinkedNode(6)
    ll_3 = DoubleLinkedNode(7)

    ll_1.set_prev(ll_2)
    ll_1.set_next(ll_3)

    print(str(ll_1))
    print(repr(ll_1))
    print()
    print("ll_2 & ll_3")
    print(str(ll_2))
    print(str(ll_3))
    print()
    print("set to none")
    ll_1.set_next(None)
    ll_1.set_prev(None)
    print(str(ll_1))
    print(str(ll_2))
    print(str(ll_3))
s