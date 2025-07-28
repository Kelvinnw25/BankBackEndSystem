from account import AccountBank
from database import databaseConnection

# Simulasi database sementara
users = {}  # key: username, value: AccountBank object

def signup():
    username = input("Enter username: ")
    if username in users:
        print("Username already exists.")
        return None
    
    password = input("Enter password: ")
    account_number = input("Enter account number: ")
    pin = input("Enter pin: ")
    new_user = AccountBank(username, password, account_number, pin=pin)
    users[username] = new_user
    print("Signup successful!")
    return new_user

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = users.get(username)
    if user and user.password == password:
        print("Login successful!")
        return user
    else:
        print("Invalid username or password.")
        return None
