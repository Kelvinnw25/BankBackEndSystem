from account import AccountBank
from database import DatabaseConnection

def signup():
    # Initialize database connection
    db = DatabaseConnection()

    # input user details
    print("\n=== Sign Up ===")
    username = input("Enter username: ")
    if db.get_account(username, ""):
        print("Username already exists. Please choose a different username.")
        return None
    
    password = input("Enter password: ")
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return None
    elif not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
        return None
    
    account_number = input("Enter account number: ")
    if db.get_account_by_number(account_number):
        print("Account number already exists. Please choose a different account number.")
        return None
    
    pin = input("Set your 6-digit pin: ")
    if len(pin) != 6 or not pin.isdigit():
        print("Pin must be exactly 6 digits.")
        return None

    # create account
    account = AccountBank(username, password, account_number, pin=pin)
    db.create_account(account.username, account.password, account.account_number, account.account_balance, account.pin)

    print("Signup successful!")
    db.close()
    return account

def login():
    # Initialize database connection
    db = DatabaseConnection()

    # input user details
    print("\n=== Login ===")    
    username = input("Enter username: ")
    password = input("Enter password: ")

    # get account from database
    data = db.get_account(username, password)
    db.close()

    if data:
        username, password, account_number, account_balance, pin = data
        print("Login successful!")
        return AccountBank(username, password, account_number, account_balance, pin)
    else:
        print("Login failed! Invalid username or password.")
        return None
