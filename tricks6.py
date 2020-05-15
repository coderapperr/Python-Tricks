class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return self.first.lower() + '.' + self.last.lower() + '@gmail.com'

    @property
    def fullname(self):
        return self.first + ' ' + self.last

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Deleting Fullname')
        self.first = None
        self.last = None
 
    def __str__(self):
        '''returns email when we try to print instance of class'''
        return self.email

    def __repr__(self):
        return self.email

emp1 = Employee('Ayush', 'Das')

print(emp1.email)
print(emp1.fullname)

emp1.fullname = 'Atharva Jangada'

print(emp1.email)
print(emp1.fullname)

del emp1.fullname