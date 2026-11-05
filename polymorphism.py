class University:
    def __init__(self):
        self.people = []

    def add_person(self, person):

        for id in self.people:
            if id.person_id == person.person_id:
                print('Same ID! Enter Unique ID')
                return

        self.people.append(person)
        print('Person Added')

        


    def display_all_people(self):

        for people in self.people:
            people.display()
        
    def process_all_payments(self):
        total = 0
        for payment in self.people:
            total += payment.calculate_payment()

        return total

        
    def search_person(self, person_id):

        for id in self.people:
            if id.person_id == person_id:
                return id

class Person:
    def __init__(self, name, person_id, email):
        self.name = name
        self.person_id = person_id
        self.__email = email

    @property
    def email_modify(self):
        return self.__email

    @email_modify.setter
    def email_modify(self, new_email):
        self.__email = new_email
        return

    def display(self):
        print(f'Person Name: {self.name} \n Person ID: {self.person_id} \n Person Email: {self.__email}')

class Student(Person):
    def __init__(self, name, person_id, email, semester, credit_hour, fee_per_credit_hour):
        super().__init__(name, person_id, email)

        self.semester = semester
        self.credit_hour = credit_hour
        self.fee_per_credit_hour = fee_per_credit_hour


    def calculate_payment(self):
        return self.credit_hour * self.fee_per_credit_hour
    
        
class Teacher(Person):
    def __init__(self,name, person_id, email, department, basic_salary, research_allowance):
        super().__init__(name, person_id, email)

        self.department = department
        self.basic_salary = basic_salary
        self.research_allowance = research_allowance

    def calculate_payment(self):
        return self.basic_salary + self.research_allowance
        
    
class AdminStaff(Person):
    def __init__(self, name, person_id, email, designation, basic_salary, transport_allowance):
        super().__init__(name, person_id, email)

        self.designation = designation
        self.basic_salary = basic_salary
        self.transport_allowance = transport_allowance


    def calculate_payment(self):
        return self.basic_salary + self.transport_allowance
    

p1 = AdminStaff('Khan', 301, 'khan@edu.pk', 'Lab Assistant', 200000, 15000)  
p2 = Student('Ali', 101, 'Ali@edu.pk', '1st', 17, 10000)
p3 = Teacher('Wali', 201, 'wali@edu.pk', 'Electrical Engineering', 300000, 100000)


log = University()

log.add_person(p1)
log.add_person(p2)
log.add_person(p3)

log.process_all_payments()


