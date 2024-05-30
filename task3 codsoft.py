class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

class ATM:
    def __init__(self, account):
        self.account = account

    def display_options(self):
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Check Balance")
        print("4. Exit")

    def withdraw(self, amount):
        if self.account.balance >= amount:
            self.account.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.account.balance}")
        else:
            print("Insufficient balance.")

    def deposit(self, amount):
        self.account.balance += amount
        print(f"Deposited {amount}. New balance: {self.account.balance}")

    def check_balance(self):
        print(f"Balance: {self.account.balance}")

def get_user_input():
    while True:
        try:
            option = int(input("Enter an option (1-4): "))
            if 1 <= option <= 4:
                return option
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number (1-4).")

def main():
    account = BankAccount(1000)
    atm = ATM(account)

    while True:
        atm.display_options()
        option = get_user_input()

        if option == 1:
            amount = float(input("Enter the amount to withdraw: "))
            atm.withdraw(amount)
        elif option == 2:
            amount = float(input("Enter the amount to deposit: "))
            atm.deposit(amount)
        elif option == 3:
            atm.check_balance()
        elif option == 4:
            print("Thank you for using the ATM.")
            break

if __name__ == "__main__":
    main()