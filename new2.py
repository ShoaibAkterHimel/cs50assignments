class Student:
    def __init__(self, name, housen, patronus):
        self.name = name
        self.houser = housen
        self.patronus= patronus
    def __str__(self):
        return f"{self.name} from {self.houser}"
    def charm(self):
        match self.patronus:
            case "Stag":
                return "horse"
    @classmethod
    def get(cls):
        name=input("name: ")
        house=input("house: ")
        patronus=input("patronus: ")
        return cls(name, house, patronus)


def main():
     student=Student.get()
     print(student)
     print(student.charm())


def get_student():
    name=input("enter your name: ")
    housex=input("enter your house: ")
    student=Student(name, housex)
    return student


main()
