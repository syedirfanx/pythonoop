x = 1
print(type(x))
print(type('Hello'))


def hello():
    print('world')


print(type(hello))

y = 'hello'
print(y.upper())


class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


d = Dog("Mug", 7)
print(type(d))
h = Dog("Tomy", 9)

print(d.get_name())
print(d.get_age())
print(h.get_name())
print(h.get_age())

h.set_age(10)
print(h.get_age())
