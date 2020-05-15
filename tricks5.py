# Python Object Oriented Programming
from datetime import date

class Employee:
    
    employee_count = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@company.com'

        Employee.employee_count += 1

    def __str__(self):
        '''returns email when we try to print instance of class'''
        return self.email

    def __repr__(self):
        return self.email

    def getFullName(self):
        return f'{self.first} {self.last}'

    def getEmail(self):
        return self.email

    def getPay(self):
        return self.pay

    def applyRaise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def setRaiseAmount(cls, raise_amount):
        cls.raise_amount = raise_amount

    @classmethod
    def setStringEmployee(cls, employeeString):
        first, last, pay = employeeString.split('-')
        return cls(first, last, int(pay))

    @classmethod
    def getEmployeeCount(cls):
        return cls.employee_count

    @staticmethod
    def isWorkingDay(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee.setStringEmployee('Ayush-Das-50000')
emp2 = Employee.setStringEmployee('Atharva-Jangada-60000')

print(emp1.getFullName())
print(emp2.getFullName())

print(emp1.getEmail())
print(emp2.getEmail())

print(emp1.getPay())
print(emp2.getPay())

Employee.setRaiseAmount(1.05)

emp1.applyRaise()
emp2.applyRaise()

print(emp1.getPay())
print(emp2.getPay())