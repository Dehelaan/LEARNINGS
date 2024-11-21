
class Employee: #class

    raise_amount = 1.04  #instance variable
    No_of_employee=0  #class variable
    def __init__(self,first,last,pay):  #instance class
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@gmail.com'

        Employee.No_of_employee+=1

    def fullname(self):  # method
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    #Constructor
    @classmethod #decorator
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp1 = Employee("Nihal","Chaudhary",1000)  #object
emp2 = Employee("Deepak","Chaudhary",500)

print(emp2.email,emp1.fullname)#
print(Employee.fullname(emp1))#Different ways to call

print(emp1.__dict__)
#emp1.raise_amount=1.05
Employee.raise_amount=1.05
print(emp1.raise_amount,emp2.raise_amount,Employee.raise_amount) #accessing class variable from instance variable
print(Employee.No_of_employee)

emp_str_1 = 'john-Doe-7000'
emp_str_2 = 'steve-Smith-8000'
emp_str_3 = 'john-Doe-7000'

new_emp_1=Employee.from_string(emp_str_1)
print(new_emp_1.email)

import datetime
my_date=datetime.date(2024,11,21)
print(Employee.is_workday(my_date)) #static method