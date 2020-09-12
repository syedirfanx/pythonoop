x = 1
print(type(x))
print(type('Hello'))


def hello():
    print('world')


print(type(hello))

y = 'hello'

print(y.upper())


class Dog:

    def __init__(self, name):
        self.name = name

    def add_one(self, x):
        return (x+1)

    def bark(self):
        print('bark!')


d = Dog("Mug")
print(type(d))
d.bark()
print(d.add_one(5))

h = Dog("Tomy")

print(d.name)
print(h.name)
