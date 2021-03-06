from abc import ABC, abstractmethod

from drivers import IStructureDriver, SimpleFileDriver


# TODO Реализовать абстрактный класс

class DriverFactoryMethod(ABC):
    @classmethod
    @abstractmethod
    def get_driver(cls) -> IStructureDriver:
        ...


class SimpleFileFactoryMethod(DriverFactoryMethod):
    DEFAULT_NAME = 'untitled.txt'

    @classmethod
    def get_driver(cls) -> IStructureDriver:
        filename = input('Введите название текстового файла: (.txt): ').strip()
        filename = filename or cls.DEFAULT_NAME
        if not filename.endswith('.txt'):
            filename = f'{filename}.txt'

        return SimpleFileDriver(filename)


if __name__ == '__main__':
    driver = SimpleFileFactoryMethod.get_driver()  # TODO с помощью фабричного метода инциализировать драйвер
    print(driver)

    write_data = [1, 2, 3]
    driver.write(write_data)

    read_data = driver.read()
    print(read_data)
