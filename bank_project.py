import random
from abc import ABC,abstractclassmethod
class Bank:
    def __init__(self,name,start_amount):
        self.name=name
        self.balance=start_amount
        self.bankrupt=False
        self.loan=0
        self.users=[]
        self.admin=[]
        self.loan=True

    def receive_loan(self,customer,amount):
        if(self.loan==True):
            if isinstance(amount,(int,float)):
                if amount > 0:
                    self.loan += amount
                    self.balance += amount
                    print(f"Loan received.Your balance now:{self.balance}")
                    customer.transaction_histroy.append(f"loan:{amount} current balace:{customer.balance}")

                else:
                    print("sorry,enter positive amount")

        else:
            print("Sorry sir .cannot give loan")
class User(ABC):
    def __init__(self,name,email,address):
        self.name=name
        self.email=email
        self.address=address
        self.bank=None

    @abstractclassmethod
    def create_account():
        raise NotImplementedError

class Customer(User):
    def __init__(self,name,email,address,account_type):
        super().__init__(name,email,address)
        self.account_type=account_type
        self.balance=0
        self.account_number=random
        self.transaction_histroy=[]
        self.loan=0
        self.loan_amount=0
        self.bank=None

    def create_account(self,bank):
        self.bank=bank
        self.bank.users.append(self)

    def deposit(self,amount):
        if(amount >0):
            self.balance +=amount
            self.bank.balance +=amount
            print(f"Deposit Succesful: {self.balance}")
            self.transaction_histroy.append(f"{amount}")
        else:
            print("Enter positive number")
    
    def take_loan(self,amount):
        if(self.loan<2):
            self.bank.receive_loan(self,amount)
        else:
            print("sorry ,loan time limit")

    def withdraw(self,amount):
        if(amount>self.balance):
            print("Sorry sir .Unavailable amount")
        else:
            self.balance-=amount
            self.bank.balance-=amount
            print(f"Withdraw succesful. Your balance now:{self.balance}")
            self.transaction_histroy.append(f"withdraw amount: {amount} balance now:{self.balance}")


    def view_balance(self):
        print(f"Your account name: {self.name}")
        print(f"your balance now:{self.balance}")

    def view_transaction_histroy(self):
        for histroy in self.transaction_histroy:
            print(histroy)
        
    def transfer(self,other,amount):
        if amount<=0:
            print("Tranfer amount should be positive")
            return
        if amount>self.balance:
            print("Insufficient Fund")
            return
        self.balance-=amount
        other.received_transfer(amount)
        self.transaction_histroy.append(f"Transfer amount: {amount} to {other.name}, balence now: {self.balance}")
    def received_transfer(self,amount):
        self.balance +=amount
        print(f"received amount :{amount}, balance now :{self.balance}")


class Admin(User):
    def __init__(self,name,email,address):
        super().__init__(name,email,address)

    def create_account(self,bank):
        self.bank=bank
        self.bank.users.append(self)

    def delete_account(self,bank,account_number):
        if bank is not None:
            index=0
            for i,user in enumerate(bank.users):
                if user.account_number==account_number:
                    bank.users.pop(i)
                    break
        else:
            print("bank not assign")

    def view_user(self):
        for user in self.bank.users:
            if isinstance(user,Customer):
                print(f"Name: {user.name}   loan:{user.loan_amount}")

    def total_balance(self):
        print(f"Total balance of bank: {self.bank.balance}")

    def view_total_loan(self):
        total_loan=0
        for user in self.bank.users:
            if isinstance(user,Customer):
                total_loan+=user.loan_amount
        print(f"Total Loan amount : {total_loan}")
    def bankrupt(self):
        if bank.balance==0:
            print("off .Bank is vanish")
        else:
            print("On.Sorry sir you cannot close the bank  beacuse the bank balnce available")

bank=Bank("Sonali bank",1000)

nahid=Customer("Md Nahid Hassan","nahid@gmail.com","Barkhada","current")
nahid.create_account(bank)
akash=Customer("Md akash mama","akash@gmail.com","Kushtia","current")
akash.create_account(bank)
biddut=Customer("Md Biddut","biddut@gmail.com","Dhaka","saving")
biddut.create_account(bank)

manager=Admin("kpi","kpi@gmail.com","Dhaka")
manager.create_account(bank)

def user_menu(customer):
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    address = input("Enter Your Address : ")
    account_type=input("Enter Your account_type  : ")
    customer = Customer(name=name, email=email, address=address,account_type=account_type)

    while True:
        print(f"Welcome to user service.")
        print("1. View balance")
        print("2. Withdraw money")
        print("3. Deposit money")
        print("4. Tranfer money")
        print("5. Transaction histroy")
        print("6. you can take loan")
        print("7. Transfer account Name and balance.")
        print("8. Exit")

        n = int(input("Enter your choice : "))
        if n==1:
            nahid.view_balance()

        elif n==2:
            withdraw_am=int(input("Enter withdraw amount: "))
            nahid.withdraw( withdraw_am)

        elif n==3:
            dep=int(input("Enter deposit amount: "))
            nahid.deposit(dep)

        elif n==4:
            amount=int(input("Enter transfer amount: "))
            nahid.transfer(akash,amount)

        elif n==5:
            nahid.view_transaction_histroy()

        elif n==6:
            amount=int(input("Enter loan amount: "))
            nahid.take_loan(amount)
        
        elif n==7:
            akash.view_balance()

        elif n==8:
            print("Exit succesfully.")
            break
        else:
            print("Invalid choice")
            break
def admin_menu(admin):
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    address = input("Enter Your Address : ")
    admin = Admin(name=name, email=email, address=address)

    while True:  
        print(" --------------- ")
        print(f"Welcome to admin service.")
        print(" --------------- ")
        print("1. View available bank balance")
        print("2. view all user")
        print("3. Delete user account")
        print("4.Total Loan amount")
        print("5. Loan freature")
        print("6. create user Account")
        print("7. Bank_rupt Status")
        print("8. Exit")

        n=int(input("Enter option: "))

        if n==1:
            manager.total_balance()

        elif n==2:
            manager.view_user()

        elif n==3:
            manager.delete_account(bank,nahid.account_number)
            print("Account delete Sucesful")

        elif n==4:
            manager.view_total_loan()

        elif n==5:
            print("Sorry sir loan freature this time Not available.")
        elif n==6:
            name = input("Enter Your Name : ")
            email = input("Enter Your Email : ")
            address = input("Enter Your Address : ")
            account_type=input("Enter Your account_type  : ")
            customer = Customer(name=name, email=email, address=address,account_type=account_type)
            customer.create_account(bank)
            print("Accout create succesful.")
        elif n==7:
            manager.bankrupt()
        elif n==8:
            print("Exit succesfully.")
            break
        else:
            print("Invalid choice")
            break


while True:
    print("Welcome Our Bank Service.")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        user_menu(Customer)
    elif choice == 2:
        admin_menu(Admin)
    elif choice == 3:
        print("Exit succesfully")
        break
    else:
        print("Invalid Input!!")




 