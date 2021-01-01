from Animal import Animal

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        return ("Meow")

    def show(self):
        return ("I am ", self.name, "and I am ", self.age, "years old ", "I am ", self.color)
