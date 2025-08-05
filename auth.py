from account import AccountBank
from database import DatabaseConnection

def signup():
    # Initialize database connection
    db = DatabaseConnection()

    # use while true to ensure valid input, as long as the condition is true, it will keep asking for input
    # input username
    while True:
        print("\n=== Sign Up ===")
        username = input("Enter username: ")
        if db.get_accountSignup(username): 
            print("Username already exists. Please choose a different username.")
        elif not username: 
            print("Username cannot be empty.")
        else: 
            break
    
    # input password
    while True:
        password = input("Enter password: ").password()
        if len(password) < 8: 
            print("Password must be at least 8 characters long.")
        elif not any(char.isdigit() for char in password): 
            print("Password must contain at least one digit.")
        else: 
            break

    # input account number
    while True:
        account_number = input("Enter account number: ")
        if db.get_account_by_number(account_number): 
            print("Account number already exists. Please choose a different account number.")
        elif not account_number.isdigit() or len(account_number) != 8:
            print("Account number must be exactly 8 digits.")
        else: 
            break
    
    # input pin
    while True:
        pin = input("Set your 6-digit pin: ")
        if len(pin) != 6 or not pin.isdigit(): 
            print("Pin must be exactly 6 digits.")
        else: 
            break

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
    data = db.get_accountLogin(username, password)
    db.close()

    if data:
        username, password, account_number, account_balance, pin = data
        print("Login successful!")
        return AccountBank(username, password, account_number, account_balance, pin)
    else:
        print("Login failed! Invalid username or password.")
        return None
