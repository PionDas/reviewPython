from Animal import Animal

class Dog(Animal):

    def __init__(self, name, age,speak):
        super().__init__(name, age)
        self.speak = speak
