class Pet:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"This is {self.name} and it is {self.age} years old")

    def speak(self):
        print("I don't know what to say")


class Cat(Pet):

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow!")

    def show(self):
        print(
            f"This is {self.name} and it is {self.age} years old and I am {self.color}")


class Dog(Pet):

    def speak(self):
        print("Bark!")


p = Pet("Tomy", 19)
p.show()
p.speak()

c = Cat("Bill", 11, "Red")
c.show()
c.speak()

d = Dog("Joe", 10)
d.show()
d.speak()
