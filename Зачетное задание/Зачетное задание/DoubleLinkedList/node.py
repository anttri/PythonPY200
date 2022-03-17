from typing import Any, Optional


class Node:
    def __init__(self, value, _next=None, _prev=None):
        self.value, self._next, self._prev = value, _next, _prev

    def __str__(self):
        return str(self.value)
s