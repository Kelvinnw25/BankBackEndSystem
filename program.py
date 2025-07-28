from database import databaseConnection
from account import AccountBank
from auth import signup, login

def run():
    print("Welcome to the ATM System!")
    user = None

    # login & signup loop
    while user is None:
        choice = input("Login or Signup?: ").lower()
        if choice == "login":
            user = login()
        elif choice == "signup":
            user = signup()
            print("please login again")
        else:
            print("Invalid choice. Please try again.")

    while True:
        user.showMenu()
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
            print("Your input invalid")



