from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    @abstractmethod
    def calculate_salary(self):
        return

class Manager(Employee):
    def __init__(self, name, id, salary, project_allownce):
        super().__init__(name, id, salary)
        self.project_allownce = project_allownce

    def calculate_salary(self):
        return super().calculate_salary()

class Develpor(Employee):
    def __init__(self, name, id, salary, travel_allownce):
        super().__init__(name, id, salary)
        self.travel_allownce = travel_allownce
    
    def calculate_salary(self):
        return self.salary + self.travel_allownce
    


e1 = Develpor('Afaq', 359, 200000, 20000)
print(e1.calculate_salary())