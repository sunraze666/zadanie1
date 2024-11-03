class Animal():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def __str__(self):
        return f"Живостное {self.name}, возраст {self.age}, вес {self.weight}"


class Dog(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
    def type_to_move(self):
        return "Бегает"

    def say(self):
        return


class Cat(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)

    def type_to_move(self):
        return "Прыгает"

    def say(self):
        return "Мяукает"

class Bird(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)

    def type_to_move(self):
        return "Летает"

    def say(self):
        return "Чирикает"

if __name__ == "__main__":
    dog = Dog(name="Шарик", age=5, weight=10)
    cat = Cat(name="Мурка", age=3, weight=5)
    bird = Bird(name="Кеша", age=4, weight=1)
    print(dog)
    print(cat)
    print(bird)

