from database import databaseConnection

class AccountBank:
    # __init__ using hinting method
    def __init__(self, username: str, password: str, account_number: str, account_balance: float = 0.00, pin: str = None):
        self.username = username
        self.password = password
        self.account_number = account_number
        self.account_balance = account_balance
        self.pin = pin

    def __str__(self): # untuk representasi string dari objek
        return f"AccountBank(username={self.username}, account_number={self.account_number}, account_balance={self.account_balance})"
    
    def show_info(self):
        print(f"Username: {self.username}\nAccount Number: {self.account_number}\nAccount Balance: {self.account_balance}")
        print("Do you want to see your pin too?")
        answer = ""
        while answer != "yes" or answer != "no":
            answer = (input("YES/NO\n")).lower()
            if answer == "yes":
                print(f"Here's your account pin: {self.pin}")
                break
            elif answer == "no":
                print("Okay, sure thanks")
                break
            else:
                print("Your input invalid")

    def balance_check(self):
        print(f"Account balance for {self.username} ({self.account_number}) is: Rp. {self.account_balance}")

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Rp. {amount} transferred to your bank account")
            print(f"Now, your account balance is: Rp. {self.account_balance:,}")
        else:
            print("amount must be positive number")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Your withdrawal of Rp. {amount} has been succesful")
            print(f"Now, your account balance is: Rp. {self.account_balance:,}")
        else:
            print(f"Withdraw failed: Your balance is insufficientor or invalid amount")

    def transfer(self, amount, recipient_account):
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            recipient_account.deposit(amount)
            print(f"Transfer to {recipient_account.username} from {self.username} has been successful")
        else:
            print("Transfer failed: Insufficient balance or invalid account")

    def showMenu(self):
        print(f"Welcome, {self.username}!")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Logout")
