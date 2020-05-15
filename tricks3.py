# Python Object Oriented Programming

class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@company.com'

    def __str__(self):
        '''returns email when we try to print instance of class'''
        return self.email

    def __repr__(self):
        return self.email

    def getFullName(self):
        return f'{self.first} {self.last}'

emp_1 = Employee('Ayush', 'Das', 50000)
emp_2 = Employee('Atharva', 'Jangada', 60000)

print(emp_1)
print(emp_1.getFullName())

print(emp_2)
print(emp_2.getFullName())

# calling methods using class name
print(Employee.getFullName(emp_1))
print(Employee.getFullName(emp_2))