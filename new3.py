class MyClass:
    all_instances = []

    def __init__(self, data):
        self.data = data
        MyClass.all_instances.append(self)

    @classmethod
    def perform_mechanism(cls):
        for instance in cls.all_instances:
            # Perform the mechanism on each instance
            print(f"Performing mechanism on instance with data: {instance.data}")

# Creating instances of MyClass
obj1 = MyClass("Data 1")
obj2 = MyClass("Data 2")

# Calling the class method to perform the mechanism on all instances
MyClass.perform_mechanism()
