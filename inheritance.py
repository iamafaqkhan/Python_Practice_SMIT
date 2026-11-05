class Employee_managment_system:
    def __init__(self, name, id, base_salary):

        self.name = name
        self.id = id
        self.base_salary = base_salary

    def display(self):
        print(f'Employee Name: {self.name} \n Employee ID: {self.id} \n Employee Base Salary: {self.base_salary}')


class Manager(Employee_managment_system):
    def __init__(self, name, id, base_salary, department, bonus):
        super().__init__(name, id, base_salary)

        self.department = department
        self.bonus = bonus

    def calculate_salary(self):
    
        return self.bonus + self.base_salary

        
class Developer(Employee_managment_system):
    def __init__(self, name, id, base_salary, prog_lang, project_allownce):
        super().__init__(name, id, base_salary)

        self.prog_lang = prog_lang
        self.project_allownce = project_allownce

    def calculate_salary(self):
        super().display()
        print(f'Employee Total Salary: {self.base_salary + self.project_allownce}')


e2 = Developer('Afaq', 359, 200000, 'AI', 20000)
e2.calculate_salary()


# e2 = Developer('Ali', 320, 150000, 'ML', 15000)
# print(e2.calculate_salary())



