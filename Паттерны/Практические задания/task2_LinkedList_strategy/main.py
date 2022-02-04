from typing import Iterable

from linked_list import LinkedList
from drivers import IStructureDriver
from factory_method import SimpleFileFactoryMethod


class LinkedListWithDriver(LinkedList):  # TODO наследовать класс LinkedList
    def __init__(self, data: Iterable = None, driver: IStructureDriver = None):
        super().__init__(data)  # TODO расширяем конструктор, чтобы в связном списке был driver
        self._driver = driver

    def read(self):
        """ С помощью драйвера считать данные и поместить их в LinkedList. """
        # TODO считать данные из драйвера

        self.clear()
        for item in self._driver.read():
            self.append(item)

    def write(self):
        """ С помощью драйвера записать данные из LinkedList. """
         # TODO записать данные с помощью драйвера
        self._driver.write(self.to_list())

if __name__ == '__main__':
    driver = SimpleFileFactoryMethod.get_driver()
    ll = LinkedListWithDriver(driver=driver)  # TODO инициализировать пустой LinkedListWithDriver
    print("Считать данные из файла input.txt")
    # TODO инициализировать драйвер и считать данные
    ll.read()
    print(ll)

    print("Записать данные в файл по умолчанию")
    # TODO заменить драйвер и записать данные
    ll.write()