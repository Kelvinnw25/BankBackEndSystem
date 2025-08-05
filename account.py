from database import DatabaseConnection

class AccountBank:
    # __init__ using hinting method
    def __init__(self, username: str, password: str, account_number: str, account_balance: float = 0.00, pin: str = None):
        self.username = username
        self.password = password
        self.account_number = account_number
        self.account_balance = account_balance
        self.pin = pin
    
    def balance_check(self):
        print(f"Account balance for {self.username} ({self.account_number}) is: Rp. {self.account_balance:,}")

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            db = DatabaseConnection()
            db.update_balance(self.account_number, self.account_balance)
            db.record_transaction(self.username, "Deposit", amount)  # record transaction
            print(f"Rp. {amount:,} transferred to your bank account")
            print(f"Now, your account balance is: Rp. {self.account_balance:,}")
            db.close()
        else:
            print("amount must be positive number")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            db = DatabaseConnection()
            db.update_balance(self.account_number, self.account_balance)

            db.record_transaction(self.username, "Withdraw", amount) #record transaction
            print(f"Your withdrawal of Rp. {amount:,} has been succesful")
            print(f"Now, your account balance is: Rp. {self.account_balance:,}")
            db.close()
        else:
            print(f"Withdraw failed: Your balance is insufficientor or invalid amount")

    def transfer(self, amount, recipient_account):
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            recipient_account.account_balance += amount

            db = DatabaseConnection()
            db.update_balance(self.account_number, self.account_balance)
            db.update_balance(recipient_account.account_number, recipient_account.account_balance)

            db.record_transaction(self.username, "Transfer", amount, recipient_account.username)  # record transaction Transfer
            db.record_transaction(recipient_account.username, "Received", amount, self.username)  # record transaction Received
            
            print(f"Rp. {amount:,} Transferred to {recipient_account.username} from {self.username} has been successful")
            print(f"Now, your account balance is: Rp. {self.account_balance:,}")
            db.close()
        else:
            print("Transfer failed: Insufficient balance or invalid account")

    def show_info(self):
        print(f"Username: {self.username}\nAccount Number: {self.account_number}\nAccount Balance: {self.account_balance}")
        print("Do you want to see your pin too?")
        answer = ""
        while answer not in ("yes", "no"):
            answer = (input("YES/NO\n")).lower()
            if answer == "yes":
                print(f"Here's your account pin: {self.pin}")
                break
            elif answer == "no":
                print("Okay, sure thanks")
                break
            else:
                print("Your input invalid")

    @staticmethod
    def get_account_object_by_number(account_number):
        db = DatabaseConnection()
        account_data = db.get_account_by_number(account_number)
        db.close()
        if account_data:
            username, password, account_number, account_balance, pin = account_data
            return AccountBank(username, password, account_number, account_balance, pin)
        return None

    def showMenu(self):
        print(f"\nWelcome, {self.username}!")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Logout")