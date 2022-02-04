
#Инкапсуляция
class A:
    def __init__(self):
        self.a = 42

    def get_a(self) -> int:
        return self.a


obj = A()

#Наследование
class Animal:

    def size(self):
        ...

    def color(self):
        ...

    def say(self):
        print("животное что-то говорит")

class Dog(Animal): #class Dog(Animal, list):
      def say(self):
          super().say() # Animal.say()
          self.color()
          print("гав-гав")

class Cat(Animal):
    def say(self):
        print("мяу-мяу")

dog = Dog()
dog.say()

cat = Cat()
cat.say()


#Полиморфизм

class Pig(Animal):
    def say(self):
        print("хрю-хрю")


def all_say(animals: List[Animal]):
    if not all(isinstance(animals, Animal) for animal in animals): #Проверка данных, что введено в список
        raise TypeError("Неправльный тип данных")

    for animal in animals:
        animal.say()

animals_list = [Dog(), Dog(), Cat(), Animal(), Pig(), list()]
all_say(animals_list)