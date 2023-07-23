#! /usr/bin/env python3
## Tutorial 04
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

        return ("{}{}{}".format(self.first,".",self.last))
    
    def apply_raise(self):
        self.pay_raise = int(self.pay* Employee.raise_amount)
        return self.pay_raise 

    def get_email(self):
        return ("{}{}{}{}".format(self.first,".",self.last,"@gmail"))
    
    #@classmethod
    #def set_rase_amt(cls,amount):
    #    cls.raise_amount=amount
    
    #@classmethod
    #def from_string(cls,emp_str):
    #    first,last,pay = emp_str_1.split('-')
    #    return cls(first,last,pay) 
    #@staticmethod
    #def is_workday(day):
        #if day.weekday()==5 or day.weekday()==6:
         #   return False
        #else:
            #return True

#import datetime
#my_date = datetime.date(2016,7,10)
#print(my_date.weekday())
#print(Employee.is_workday(my_date))

class Developer(Employee):
    def __init__(self, first, last, pay,prog_long):
        super().__init__(first,last,pay)
        self.prog_long = prog_long

class Manager(Employee):
    def __init__(self,first,last,pay,employees =None):
        super().__init__(first,last,pay)
        #self.employees = employees
        if employees is None:
            self.employees = []
        else:
            self.employees = employees


    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
        else:
            return "already in the list"

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
        else:
            return "Not in the list"
    
    def print_emps(self):
        for emp in self.employees:
            print("---->",emp.fullname())

    def print_email(self):
        for emp in self.employees:
            print("---->",emp.get_email())






#print(help(Developer))
dev_1 = Employee("Corey","Schafer",50000)

dev_1 = Developer("Corey","Schafer",50000,"Python")
dev_2 = Developer("Corey2","Schafer2",50000,"Java")
#dev_2 = Developer("Test","User",60000)
print(dev_1.prog_long)
print(dev_2.prog_long)
mrg_1 = Manager("Sue","Smith",90000,[dev_1])


mrg_1.print_emps()
mrg_1.add_emp(dev_2)
print('------')
mrg_1.print_emps()
mrg_1.print_email()