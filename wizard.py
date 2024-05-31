class Wizard:
    def __init__(self, name):
        self.nam=name
class Student(Wizard):
    def __init__(self, nam, house):
        super().__init__(nam)
        self.house=house
class Professor(Wizard):
    def __init__(self, naam, subject):
        super().__init__(naam)
        self.subject=subject

professor=Professor("Albus", "Manage")
print(professor.nam)
