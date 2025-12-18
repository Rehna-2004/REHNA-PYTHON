class bankaccount():
    def __init__(self,accno,accname,acctype,accbala):
        self.accno=accno
        self.accname=accname
        self.acctype=acctype
        self.accbala=accbala
    def deposit(self,amount):
        self.accbala+=amount
        print("Current balance=", self.accbala)
        print("Amount deposited:",amount)
    def accountinfo(self):
        print("Account Number=",self.accno)
        print("Account Name=",self.accname)
        print("Account Type=",self.acctype)
        print("Account Balance=",self.accbala)
    def withdraw(self,amount):
        if amount>self.accbala:
          print("Insufficient balance!")
        else:
           self.accbala -= amount 
           print("Withdrawn:",amount)
           print("remaining balance",self.accbala)

no=int(input("Enter the account number:"))
name=input("Enter the account name:")
acctype=input("Enter the account type:")
bal=float(input("Enter the account balance:"))
obj=bankaccount(no,name,acctype,bal)
depo=int(input("Enter the amount to be deposited:"))
obj.deposit(depo)
wid=int(input("Enter the withdrawal amount:"))
obj.withdraw(wid)

