#! /usr/bin/env python3
## Tutorial 02
#name,emal,paid
class Employee:
    raise_amount = 1.04
    num_of_emps = 0
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last 
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"
        Employee.num_of_emps += 1
    
    def fullname(self):

        return ("{} {}".format(self.first,self.last))
    
    def apply_raise(self):
        self.pay_raise = int(self.pay* Employee.raise_amount)
        return self.pay_raise 


emp_1 = Employee("Corey","Schafer",50000)
emp_2 = Employee("Test","User",60000)



#print(emp_1.email)
#print("{} {}".format(emp_1.first,emp_2.first))
#print(emp_1.fullname())
#print(Employee.fullname(emp_1))
#print(emp_1.apply_raise())
#print(emp_1.pay)
#print(emp_1.__dict__)
#print(Employee.__dict__)
#print(emp_1.raise_amount)
#print(Employee.raise_amount)
#Employee.raise_amount = 1.05
#print(emp_2.raise_amount)
print(Employee.num_of_emps)