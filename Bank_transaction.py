class Bank_account:
    def __init__(self,account_no,name,balance):
        self.account_no=account_no
        self.name=name
        self.__balance=balance

    @property
    def check_balance(self):
        return self.__balance
    
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            return self.__balance
        else:
            raise ValueError("Enter the correct amount")
    
    def withdrawel(self,amount):
        if self.__balance>=amount:
            self.__balance-=amount
            return self.__balance
        else:
            raise ValueError("insufficient balance")

    def showdetails(self):
        return f"*****account_no:{self.account_no}*****\n*****Name:{self.name}*****\n*****balance:{self.__balance}*****"

a=Bank_account(123456789," Sravan",10000)
while True:
    print("Bank Transaction Menu")
    print("1.deposit")
    print("2.withdrawel")
    print("3.check_balance")
    print("4.showdetails")
    print("5.exit")

    choice=int(input("enter the choice:"))
    if choice==1:
        amount=int(input("enter the amount to be deposited:"))
        print(a.deposit(amount))
    elif choice==2:
        amount=int(input("enter the amount to be withdrawn:"))
        print(a.withdrawel(amount))
    elif choice==3:
        print(a.check_balance)
    elif choice==4:
        print(a.showdetails())
    elif choice==5:
        break
