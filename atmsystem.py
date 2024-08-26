class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount} withdrawn successfully. Remaining balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def change_pin(self, old_pin, new_pin):
        if self.pin == old_pin:
            self.pin = new_pin
            print("PIN changed successfully.")
        else:
            print("Incorrect old PIN.")

class ATM:
    def __init__(self, account):
        self.account = account

    def authenticate(self, pin):
        return self.account.pin == pin

    def display_menu(self):
        print("ATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")

    def run(self):
        print("Welcome to the ATM!")
        attempts = 0
        while attempts < 3:
            pin = input("Enter your PIN: ")
            if self.authenticate(pin):
                while True:
                    self.display_menu()
                    choice = input("Choose an option: ")
                    if choice == '1':
                        print(f"Your current balance is: {self.account.check_balance()}")
                    elif choice == '2':
                        amount = int(input("Enter amount to deposit: "))
                        self.account.deposit(amount)
                    elif choice == '3':
                        amount = int(input("Enter amount to withdraw: "))
                        self.account.withdraw(amount)
                    elif choice == '4':
                        old_pin = input("Enter your old PIN: ")
                        new_pin = input("Enter your new PIN: ")
                        self.account.change_pin(old_pin, new_pin)
                    elif choice == '5':
                        print("Thank you for using the ATM. Goodbye!")
                        break
                    else:
                        print("Invalid option. Please try again.")
                break
            else:
                attempts += 1
                print(f"Incorrect PIN. You have {3 - attempts} attempt(s) left.")
        if attempts == 3:
            print("Your account is locked due to too many failed attempts.")

user_account = Account(account_number="123456789", pin="1234", balance=1000)

atm_machine = ATM(user_account)

atm_machine.run()