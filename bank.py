class Bankaccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Your amount {amount} successfully deposited, thank you!")
        else:
            print("Deposit amount should be positive.")

    def withdraw(self, withdraw_amount):
        if withdraw_amount <= self.balance:
            self.balance -= withdraw_amount
            print(f"You have successfully withdrawn the amount of {withdraw_amount}. Current balance: {self.balance}")
        else:
            print('Insufficient funds.')

    def check_balance(self):
        print(f"Your current balance: {self.balance} Rupees.")


# user interaction
bank_account = None  

while True:
    print( "*****************  Welcome to my bank online services  ************************")
    print("1. Create a bank account")

    print("2. Deposit money")

    print("3. Withdraw money")

    print("4. Check balance")

    print("5. Exit")

    count = int(input("Select an option (1-5): "))

    if count == 1:
        name = input("Enter your name: ")
        balance = int(input("Enter opening balance: "))
        bank_account = Bankaccount(name, balance)
        print(f"Hello {name}, thank you for creating an account!")

    elif count == 2:
        if bank_account:
            amount = int(input("Enter the amount to deposit: "))
            bank_account.deposit(amount)
        else:
            print("Please create an account first.")

    elif count == 3:
        if bank_account:
            withdraw_amount = int(input("Enter the amount to withdraw: "))
            bank_account.withdraw(withdraw_amount)
        else:
            print("Please create an account first.")

    elif count == 4:
        if bank_account:
            bank_account.check_balance()
        else:
            print("Please create an account first.")
    
    elif count == 5:
        print("Exiting the program.")
        break

    else:
        print("Invalid option. Please select a valid option between 1-5.")
