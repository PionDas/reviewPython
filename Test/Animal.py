class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("no Sound")

    def show(self):
        print("Animal: ", self.name, "\nAge: " , self.age, "\nSound:", self.speak)
