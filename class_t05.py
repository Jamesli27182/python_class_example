#! /usr/bin/env python3
## Tutorial 05
#name,emal,paid
class Employee:
    raise_amount = 1.04
    num_of_emps = 0
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last 
        self.pay = pay
        self.email = self.first + "." + last + "@gmail.com"
        Employee.num_of_emps += 1
    
    def fullname(self):

        return ("{}{}{}".format(self.first,".",self.last))
    
    def apply_raise(self):
        self.pay_raise = int(self.pay* Employee.raise_amount)
        return self.pay_raise 

    def get_email(self):
        return ("{}{}{}{}".format(self.first,".",self.last,"@gmail"))
    
    def __repr__(self):
        return "Employee({},{},{})".format(self.first,self.last,self.pay)

    def __str__(self):
        return "Employee({},{})".format(self.fullname(),self.email)


emp_1 = Employee("Corey","Schafer",50000)
print(emp_1)
emp_2 = Employee("Test","User",60000)
print(emp_2)
print(repr(emp_1))
print(str(emp_1))
print(emp_1.__repr__)



