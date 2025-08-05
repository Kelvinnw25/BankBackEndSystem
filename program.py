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
            amount = float(input("Enter amount to transfer: "))
            recipient_account_number = input("Enter recipient account number: ")

            attempt = 0
            while attempt < 3:
                pinInput = input("Enter your 6-digit pin: ")
                if pinInput == user.pin:
                    recipient_account = AccountBank.get_account_object_by_number(recipient_account_number)
                    if recipient_account:
                        user.transfer(amount, recipient_account)
                        break
                    else:
                        print("Recipient account not found.")
                        break
                else:
                    attempt += 1
                    print(f"Incorrect pin. You have {3 - attempt} attempts left.")

        elif option == 5:
            db = DatabaseConnection()
            transactions = db.get_transaction_history(user.username)
            db.close()

            print("\n=== Transaction History ===")
            for type, amount, target_account, timestamp in transactions:
                if target_account:
                    if type == "Transfer":
                        print(f"{timestamp} | {type} of Rp. {amount:,} to {target_account}")
                    elif type == "Received":
                        print(f"{timestamp} | {type} of Rp. {amount:,} from {target_account}")
                else:
                    print(f"{timestamp} | {type} of Rp. {amount:,}")

        elif option == 6:
            print("Logging out...\n")
            run()  #restart
            
        else:
            print("Your input invalid")