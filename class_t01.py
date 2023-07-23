#! /usr/bin/env python3
## Tutorial 01
#name,emal,paid
class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last 
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"
    
    def fullname(self):

        return ("{} {}".format(self.first,self.last))
    pass


emp_1 = Employee("Corey","Schafer",50000)
emp_2 = Employee("Test","User",60000)



print(emp_1.email)
print("{} {}".format(emp_1.first,emp_2.first))
print(emp_1.fullname())
print(Employee.fullname(emp_1))
