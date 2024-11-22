
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

class Developer(Employee):  #INHERITANCE of Employee class
    raise_amount= 1.10

    def __init__(self, first, last, pay,prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang =prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees


    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->',emp.fullname())

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


dev_1=Developer("Nihal","Chaudhary",1000,'python')  #object
dev_2 = Developer("Deepak","Chaudhary",5000,'R')

print(dev_1.email,dev_2.email)
#print(help(Developer ))
print(dev_2.pay)
dev_2.apply_raise()
print(dev_2.pay)

mng_1=Manager('sue','smith',9000,[dev_1])

print(mng_1.email)

mng_1.add_emp(dev_2)
mng_1.print_emp()
mng_1.remove_emp(dev_1)
mng_1.print_emp()

print(isinstance(mng_1,Employee))
print(issubclass(Manager,Employee))