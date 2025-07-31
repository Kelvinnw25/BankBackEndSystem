from database import DatabaseConnection
from account import AccountBank
from auth import signup, login

def run():
    print("Welcome to the ATM System!")
    user = None

    while user is None:
        choice = input("Login or Signup?: ").lower()
        if choice == "login":
            user = login()
        elif choice == "signup":
            user = signup()
            print("\nPlease login again")
            run()  #restart
        else:
            print("Invalid choice. Please try again.")

    while True:
        user.showMenu()
        option = int(input("Enter your option: "))
        if option == 1:
            user.balance_check()
        elif option == 2:
            user.deposit(float(input("Enter amount to deposit: ")))
        elif option == 3:
            user.withdraw(float(input("Enter amount to withdraw: ")))
        elif option == 4:
            user.transfer(float(input("Enter amount to transfer: ")), (input("Enter recipient's account number: ")))
        elif option == 5:
            print("nih historynya")
        elif option == 6:
            print("Logging out...\n")
            user.db.close()
            run()  #restart
        else:
            print("Your input invalid")