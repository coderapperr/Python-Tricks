# Python Object Oriented Programming

class Employee:
    
    raise_amount = 1.04
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

    def applyRaise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Ayush', 'Das', 50000)
emp_2 = Employee('Atharva', 'Jangada', 60000)

emp_1.applyRaise()
emp_2.applyRaise()

print(emp_1.pay)
print(emp_2.pay)

print(Employee.employee_count)