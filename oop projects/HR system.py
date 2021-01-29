class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email= first + '_' + last + "@gmail.com"

    def fullname(self):
        return (f'{self.first} {self.last}')


class Developer(Employee):
    def __init__(self,first,last,pay,language):
        super(). __init__(first,last,pay)
        self.language=language


class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super(). __init__(first,last,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees

    def addemp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def removeemp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)


    #show employees under a manager
    def show(self):
        for emp in self.employees:
            print('--->',emp.fullname())

dev1=Developer('Vincent','Ko',15000,'Python')
dev2=Developer('James','Li',20000,'Java')
mg1=Manager('Ji','So',40000,[dev1])

mg1.addemp(dev2)
mg1.show()
