#! /usr/bin/env python3
## Tutorial 06
#name,emal,paid
class Employee:
    raise_amount = 1.04
    num_of_emps = 0
    def __init__(self,first,last):
        self.first = first
        self.last = last 
        self.email = self.first + "." + last + "@gmail.com"
        Employee.num_of_emps += 1
    
    @property
    def fullname(self):

        return ("{}{}{}".format(self.first,".",self.last))
    
    def get_email(self):
        return ("{}{}{}{}".format(self.first,".",self.last,"@gmail"))
    
    @fullname.setter
    def fullname(self,name):
        first , last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("deleted")
        self.first = None
        self.last = None

emp_1 = Employee("John","Smith")
print(emp_1.fullname)
print(emp_1.get_email())
emp_1.first = "Jim"
print(emp_1.fullname)
print(emp_1.get_email())
emp_1.fullname = "Jim Smith"
print(emp_1.fullname)
print(emp_1.get_email())
del emp_1.fullname

