#ПРИМЕРЫ ПАТЕРНОВ
#singltone
#if foo is None ... None это пример singltone
#class Cinfig(): это singltone

#итератор
#for i in range(100):
#    ...

#синтатический сахар
#def deco(func):
#    def wraper(*args, **kwargs)
#        return  func(*args, **kwargs)
#    return wraper
#@deco
#def some_func
#    ...
#
#some_func = deco(some_func)

from typing import Iterator

class SomeClassIterator:

    def __init__(self, sc: "SomeClass"):
        self.sc = sc
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.sc.get_item(self.i)
        except IndexError:
            raise StopIteration

        self.i +=1
        return item

class SomeClass:
    def __init__(self):
        self._l = list(range(10))

    def get_item(self, index: int):
        return self._l[index]

    #def __iter__(self) -> Iterator:
    #    return SomeClassIterator(self)

    def __iter__(self) -> Iterator:
        i = 0
        while True:
            try:
                yield self.get_item(i)
            except IndexError:
                return
            i += 1


#class SomeBadClass: #Класс который будет не правильно работать. Итераторы в нем не будут не зависимыми.
#    def __init__(self):
#        self._l = list(range(10))
#
#    def get_item(self, index: int):
#        return self._l[index]
#
#    def __iter__(self) -> Iterator:
#        return self
#
#    def __next__(self):
#        try:
#            item = self.sc.get_item(self.i)
#        except IndexError:
#            raise StopIteration
#        self.i +=1
#        return item


sc = SomeClass()
iterator = iter(sc) # for i in sc:
iterator0 = iter(sc)
iterator1 = iter(sc)
for i in iterator:
    print(i)

#создается sc
#for:
#iterator = sc.__iter__ #iter
#iterator,__next__ #next