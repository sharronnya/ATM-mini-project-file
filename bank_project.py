# this is a basic banking system implementataion in python that allows users to create account, log in deposits 
# and withdraw funds,check balances and view mini statement.
#the system consists of two classes:account and banking system.

# -----------BANKING SYSTEM---------

class Account:
    def __init__(self, username, password, balance=0,):

        self.username = username
        self.password = password
        self.balance = balance
        self .get_mini_statement = []

# the account class is  defined with three instance varaibles - username,password and balance.
# the __init__ method initializes three varaibles with arguments passed while craetin an object of this class
# the class also contains four methods -deposit ,withdraw, get_balance, and get_mini_statement.

    def deposit(self, amount):

        self.balance += amount
        print(f"\nAmount deposited: {amount}\nTotal Balance:{self.balance}")

#the deposit method takes an arguement amount and adds it to the balance varaiable.
#it then prints a message showing the deposited amount and thae updated balance.

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"\nAmount Withdrawn:{amount}\nRemaining Balance:{self.balance}")
        else:
            print("Insufficient balance")

#the withdraw method takes an argument amount and checks if the balance is greater than or eqaul to the amount
# to be withrawn amount from the balance and prints a message showing the withdrawn amount and the updated balnce.
# if not it prints a message saying that there is insufficient  balance.

    def get_balance(self):
        return self.balance

#the get balance simply returns the current balance.

    def get_mini_statement(self):
        print("Mini statement:")
        print(f"Username:{self.username}")
        print(f"Current balance:{self.balance}")

#the get_mini_statement prints the username and current balance of the account.


class BankingSystem:
    def __init__(self):
        self . accounts = {}

# the bankingsystem class is defined.
# it has one instance varaible accounts.
# which is the dictionary that stores the username.
# as key and the account object as value.

    def create_account(self,username, password):
        if username in self.accounts:
            print("Username already exists")
        else:
            self.accounts[username] = Account(username,password)
            print("\nAccount created successfully")
            print("-------Welcome to PYTHON Bank------") 

# the create accounts takes two arguments - username and password.
# it checks if the username already exists if it does not it creates new account
# object with the given username and password and adds it to the accounts dictionary.
# it then prints a message saying that the account was created succesfully.

    def login(self, username, password):
        if username in self.accounts:
            account = self.accounts[username]
            if account.password == password:
                print("Login sucess....")
                return account
            else:
                print("Invalid Password")
        else:
            print("Invalid username")
            return None

# the login method takes two arguments - username and password.
# it checks if the given username exists in the account dictionary.
#if it does it retrive the corresponding account objects and checks if the given password matches the password 
# of the account
#if it does it prints maessage saying that the loggin was succesfull and returns the account object
#if it does not it prints a message saying that the password is invalid
#if the given username is not foundn in the acounts dictionary
#it print  a message saying that username is invalid...

bank = BankingSystem()

while True:
    print("\n")
    print("1. Create account")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice(1-3): ")

# the  main program loop is defined inside the if __name__ == '__main__':
# block. it creates a new Bankingsystem object and presents a menu of options to the user
# create an account, login, or exit.

    if choice == '1':
        username = input("Enter username: ")
        password = input("Enter password: ")
        bank.create_account(username,password)

# if the user chooses to create an account the program prompts the user to enter a username and password,
# it then calls the create_account method of the banking system object with these arguments.

    elif choice == '2':
        username = input("Enter username: ")
        password = input("Enter password: ")
        account = bank.login(username, password)

        if account is not None:
            while True:
                print("\n------Welcome to PYTHON Bank------")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check balance")
                print("4. Mini statement")
                print("5. Logout\n")
                choice = input("Enter your choice (1-5): ")

# if the user chooses to login the program prompts the user to enter thier username and password
# it then calls the login method of the banking system  objectvwith these arguments.
# if the login is succesfull it presents the user with a menu of options - 
# deposit withdraw check balance, print mini_statement,or logout.

                if choice == '1':
                    amount = int(input("Enter amount to deposit:"))
                    account.deposit(amount)

                elif choice == '2':
                    amount = int(input("Enter amount to withdraw:"))
                    account.withdraw(amount)

#if the user chooses to deposit or withdraw, the program prompts the user to enter the amount to
# deposit or withdraw,
# it then calls the corresponding method of the account object.....

                elif choice == '3':
                    print(F"current balance:{account.get_balance()}")

#if the user chooses to checkn thier balance the program calls the get_baalnced method
#of the account object and prints the current balance.

                elif choice == '4':
                    account.get_mini_statement()

#if the user chooses to print a mini-statement the program calls the get_mini_statement
# method of the account object and prints the username and current balance.

                elif choice == '5':
                    print("\n---------THANK YOU VISIT AGAIN--------")
                    break

# if the user chooses to logout, break out of the inner while loop
# and display a message saying "THANK YOU VISIT AGAIN".

                else:
                    print("Invalid choice")

    elif choice == '3':
        print("\n--------THANK YOU------")
        break

#if the user selects option 3, a message is printed indicating that they have excited the program
# and the break statememt is used to  exit the outer while loop that displays the main menu.

    else:
        print("Imvalid choice")

#-------------- FINISHED -------- THANK YOU-------------------                                                                    

                        
                 
         
     

                
 
                          
              
 
              
 
  
         

        