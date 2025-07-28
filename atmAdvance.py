from database import DatabaseConnection

class AccountBank:
    def __init__(self, username, password, account_number, account_balance=0, pin="123456"):
        self.username = username
        self.password = password
        self.account_number = account_number
        self.account_balance = account_balance
        self.pin = pin
        self.save_to_file("database.txt")

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

    def showMenuGuest(self):
        print("Welcome to the ATM System!")
        choice = input("Login or Signup?: ").lower()

    def showMenuUser(self):
        print(f"Welcome, {self.username}!")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Logout")

    def run(self):
        self.showMenuGuest()
        if choice == "login":
            usernameInput = input("Enter your username: ")
            passwordInput = input("Enter your password: ")
        elif choice == "signup":
            usernameInput = input("Enter your username: ")
            passwordInput = input("Enter your password: ")
            account_number = input("Enter your account number: ")
            pin = input("Enter your pin: ")
            new_account = AccountBank(usernameInput, passwordInput, account_number, pin=pin)
            print(f"Account created successfully for {usernameInput}!")
            return new_account

        option = 0
        while True:
            self.showMenuUser()
            option = int(input("Enter your option: "))
            if option == 1:
                print("saldo lu sekian...")
            elif option == 2:
                print("udah masuk gan")
            elif option == 3:
                print("udah keluar gan")
            elif option == 4:
                print("udah kekirim gan")
            elif option == 5:
                print("nih historynya")
            elif option == 6:
                print("Logging out...")
                break
            else:
                print("Your input isn't valid")




# Example usage



