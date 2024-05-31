class Person:
    def __init__(self, age, name):
        self.name = name
        self.age = age

# Creating a new Person object
p1 = Person("Alice", 30)

# Accessing attributes of the Person object
print("Name:", p1.name)
print("Age:", p1.age)
