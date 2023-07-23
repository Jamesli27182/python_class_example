#! /usr/bin/env python3
## Tutorial 03
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
    @classmethod
    def set_rase_amt(cls,amount):
        cls.raise_amount=amount
    
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay) 
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        else:
            return True

import datetime
my_date = datetime.date(2016,7,10)
print(my_date.weekday())
print(Employee.is_workday(my_date))
print(help(Deve))



#emp_1 = Employee("Corey","Schafer",50000)
#emp_2 = Employee("Test","User",60000)

#emp_str_1 = "John-Doe-70000"
#first,last,pay = emp_str_1.split('-')
#new_emp1 = Employee.from_string(emp_str_1 )
#print(new_emp1.first)
#print(new_emp1.last)
#print(new_emp1.pay)
