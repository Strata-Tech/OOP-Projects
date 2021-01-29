class User:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender


    def show(self):
        print('Welcome')
        print('')
        print('Personal Details')
        print(f'Name:{self.name}')
        print(f'Gender: {self.gender}')
        print(f'Age: {self.age}')

class Bank(User):
    def __init__(self,name,age,gender):
        super(). __init__(name,age,gender)
        self.balance=0


    def deposit(self,amount):
        self.balance=self.balance + amount
        print(f' Account balance updated, you have $ {self.balance}')

    def withdraw(self,amount):
        if self.balance<amount:
            print(f'Insufficient balance , you only have {self.balance}')
        else:
            self.balance=self.balance-amount
            print(f' Account balance updated, you have $ {self.balance}')

    def BalanceEnquiry(self):
        print(f' Account balance , you have $ {self.balance}')

jack=Bank('Jack Tan',30,'male')
jack.deposit(1000)
jack.withdraw(90)
jack.show()
jack.BalanceEnquiry()




