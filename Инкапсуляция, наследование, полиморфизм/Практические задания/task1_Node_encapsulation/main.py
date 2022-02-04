from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
                # _ Значит - не менять атрибут
                # __ Значит - не менять атрибут
        self._next = None  # TODO заменить на private
        self.set_next(next_)

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self._next is None else f"Node({self.value}, Node({self._next}))"  # TODO заменить на private

    def __str__(self) -> str:
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    def set_next(self, next_: Optional["Node"] = None) -> None:
        self.is_valid(next_)
        self._next = next_  # TODO заменить на private

#class A:
#    def __init__(self):
#        self.a = 4
#        self._a = 8
#        self.__a = 15 #Используют для наследования
#
#class C:
#    def __init__(self):
#        self.__a = 16 #Если не переопределять a
#
#class B(A, C):
#    def __init__(self):
#        super().__init__()
#        print(self._A__a)

if __name__ == "__main__":
    first_node = Node("first_node")
    second_node = Node("second_node")
    print(first_node._next)

    first_node.set_next(second_node)

    print(repr(first_node), repr(second_node))

#    a = A()
#        # [_A__a, _a, a]
#    print(a._A__a)
#