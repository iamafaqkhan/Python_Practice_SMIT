# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.__marks = marks

#     @property
#     def modify(self):
#         return self.__marks

#     @modify.setter
#     def modify(self, new_marks):

#         if new_marks < self.__marks:
#             return 'Enter value b/w 0-100'
#         else:
#             self.__marks = new_marks

#     def get_grade(self):

#         if self.__marks >= 90:
#             return 'A'
#         elif self.__marks >= 80:
#             return 'B'
#         elif self.__marks >= 70:
#             return 'C'
#         elif self.__marks >= 60:
#             return 'D'
#         else:
#             return 'F'

# s1 = Student('Ali', 78)
# s2 = Student('Gul', 98)
# s3 = Student('Rehmat', 67)


# print(f'Student Name: {s1.name} Student Marks: {s1.modify} Student Grade: {s1.get_grade()}')
# print(f'Student Name: {s2.name} Student Marks: {s2.modify} Student Grade: {s2.get_grade()}')
# print(f'Student Name: {s3.name} Student Marks: {s3.modify} Student Grade: {s3.get_grade()}')


## Bank Example

class BankAccount:
    def __init__(self,  account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    @property
    def modify(self):
        return self.__balance

    @modify.setter
    def modify(self, new_amount):

        if new_amount < 0:
            return 'enter value greater than 0'
        else:
            self.__balance = new_amount

    def deposit(self, amount):

        self.__balance += amount

        return self.__balance
    def withdraw(self, amount):

        self.__balance -= amount

        return self.__balance

    def transfer(self, reciever, money):

        if self.__balance < money:
            return 'Insufficient Amount to Send'

        else:
            self.__balance -= money
            reciever.__balance += money



a1 = BankAccount('Afaq', 10000)
a2 = BankAccount('Ali', 5000)

a1.transfer(a2, 2000)







print(f'Account Holder: {a1.account_holder} Amount: {a1.modify}')
print(f'Account Holder: {a2.account_holder} Amount: {a2.modify}')







        




    
        

