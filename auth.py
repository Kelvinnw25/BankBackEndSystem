from account import AccountBank
from database import DatabaseConnection

def signup():
    # Initialize database connection
    db = DatabaseConnection()

    # input user details
    print("\n=== Sign Up ===")
    username = input("Enter username: ")
    password = input("Enter password: ")
    account_number = input("Enter account number: ")
    pin = input("Set your 6-digit pin: ")

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
