class Bank :
    def __init__(self,username,pan,address):
        self.username=username
        self.pan=pan
        self.address=address
        self.balance=0.0
        print(f'Hello { self.username} ;) Your account created successfully ! ')

    def depposit(self,amount):
        self.balance=self.balance+amount
        print(f'{amount}  depposited successfuly ;)')

    def withdraw(self,amount):
        if amount<self.balance:
            self.balance=self.balance-amount
            print(f'{amount} withdraw successfully')
        else:
            print('incomplete fund')

    def ministratment(self):
        print(f'Your Account balance is {self.balance}')

username=input('Enter your Name : ')
pan=input('Enter your Pan : ')
address=input('Enter your Address : ')
bank=Bank(username,pan,address)

while True:
    print('\nPlease Select any Option : ')
    print('1.Depposit\n2.Withdraw\n3.Ministratment\n4.Stop')
    option=int(input(''))
    
    if option==1:
        amount=float(input('Enter Deposited amount : '))
        bank.depposit(amount)

    elif option==2:
        amount=float(input('Enter Withdraw amount : '))
        bank.withdraw(amount)

    elif option==3:
        bank.ministratment()

    elif option==4:
        print('Goodbye and hope you enjoy ;)')
        break

    else:
        print('Invalid Option :( ')
