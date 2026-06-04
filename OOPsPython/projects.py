import json
import random
from pathlib import Path


class Bank:

    database = Path(__file__).parent / "data.json"

    # Load existing data
    try:
        if database.exists():
            with open(database, "r") as file:
                data = json.load(file)
        else:
            data = []

    except (json.JSONDecodeError, FileNotFoundError):
        data = []

    @staticmethod
    def update():
        try:
            with open(Bank.database, "w") as file:
                json.dump(Bank.data, file, indent=4)

        except Exception as err:
            print(f"Error saving data: {err}")

    def create_account(self):

        print("\n========== CREATE ACCOUNT ==========\n")

        try:
            age = int(input("Enter Age            : "))
        except ValueError:
            print("Age must be a number.")
            return

        name = input("Enter Name           : ")
        email = input("Enter Email          : ")
        pin = input("Enter 4-Digit PIN    : ")

        if age < 18:
            print("\nYou must be at least 18 years old.")
            return

        if len(pin) != 4 or not pin.isdigit():
            print("\nPIN must contain exactly 4 digits.")
            return

        account_number = random.randint(10000000, 99999999)

        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "account_number": account_number,
            "balance": 0
        }

        Bank.data.append(info)
        Bank.update()

        print("\n" + "=" * 50)
        print("      ACCOUNT CREATED SUCCESSFULLY")
        print("=" * 50)
        print(f"Name           : {name}")
        print(f"Age            : {age}")
        print(f"Email          : {email}")
        print(f"Account Number : {account_number}")
        print(f"Balance        : ₹0")
        print("=" * 50)

    def deposit_money(self):

        print("\n========== DEPOSIT MONEY ==========\n")

        try:
            account_number = int(input("Enter Account Number : "))
            pin = input("Enter PIN            : ")
            amount = float(input("Enter Amount         : ₹"))

        except ValueError:
            print("Invalid Input!")
            return

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        for account in Bank.data:

            if (
                account["account_number"] == account_number
                and account["pin"] == pin
            ):

                account["balance"] += amount

                Bank.update()

                print("\n" + "=" * 50)
                print("         DEPOSIT SUCCESSFUL")
                print("=" * 50)
                print(f"Deposited Amount : ₹{amount}")
                print(f"Current Balance  : ₹{account['balance']}")
                print("=" * 50)

                return

        print("\nInvalid Account Number or PIN.")

    def withdraw_money(self):

        print ("===========WITHDRAW MONEY============")

        try:
            account_number = int(input("Enter Account Number : "))
            pin = input("Enter PIN            : ")
            amount = float(input("Enter Amount         : ₹"))

        except ValueError:
            print("Invalid Input!")
            return
        
        if amount <= 0 :
            print("Amount must be Greater then Zero")
            return
        

        for account in Bank.data:

            if (
                account["account_number"] == account_number
                and account["pin"] == pin
            ):
                if amount > account["balance"]:
                    print("Insufficient Balance!")
                    return
                account["balance"] -= amount

                Bank.update()

                print("\n" + "=" * 50)
                print("         WITHDRAW SUCCESSFUL")
                print("=" * 50)
                print(f"Deposited Amount : ₹{amount}")
                print(f"Current Balance  : ₹{account['balance']}")
                print("=" * 50)

                return

        print("\nInvalid Account Number or PIN.")

    
    def view_details(self):
        print("\n ===========ACCOUNT DEATILS ===========\n")

        try:
            account_number = int(input("Enter Account Number :"))
            pin = input ("Enter PIN")
        except ValueError:
            print("Invalid Input")
            return
        
        for account in Bank.data:

            if (
                account["account_number"] == account_number
                and account["pin"] == pin
            ):

                print("\n" + "=" * 50)
                print("            ACCOUNT DETAILS")
                print("=" * 50)
                print(f"Name           : {account['name']}")
                print(f"Age            : {account['age']}")
                print(f"Email          : {account['email']}")
                print(f"Account Number : {account['account_number']}")
                print(f"Balance        : ₹{account['balance']}")
                print("=" * 50)

                return

        print("Invalid Account Number or PIN.")

    def update_details(self):

        print("\n========== UPDATE DETAILS ==========\n")

        try:
            account_number = int(input("Enter Account Number : "))
            pin = input("Enter Current PIN    : ")

        except ValueError:
            print("Invalid Input!")
            return

        for account in Bank.data:

            if (
                account["account_number"] == account_number
                and account["pin"] == pin
            ):

                print("\nWhat do you want to update?")
                print("1. Name")
                print("2. Email")
                print("3. PIN")

                choice = int(input("Enter Choice : "))

                if choice == 1:
                    account["name"] = input("Enter New Name : ")

                elif choice == 2:
                    account["email"] = input("Enter New Email : ")

                elif choice == 3:

                    new_pin = input("Enter New PIN : ")

                    if len(new_pin) != 4 or not new_pin.isdigit():
                        print("PIN must be exactly 4 digits.")
                        return

                    account["pin"] = new_pin

                else:
                    print("Invalid Choice")
                    return

                Bank.update()

                print("\nDetails Updated Successfully!")

                return

        print("Invalid Account Number or PIN.")

    def delete_account(self):

        print("\n========== DELETE ACCOUNT ==========\n")

        try:
            account_number = int(input("Enter Account Number : "))
            pin = input("Enter PIN            : ")

        except ValueError:
            print("Invalid Input!")
            return

        for account in Bank.data:

            if (
                account["account_number"] == account_number
                and account["pin"] == pin
            ):

                print("\nACCOUNT FOUND")
                print(f"Name    : {account['name']}")
                print(f"Email   : {account['email']}")
                print(f"Balance : ₹{account['balance']}")

                confirm = input(
                    "\nAre you sure you want to delete this account? (Y/N): "
                ).upper()

                if confirm == "Y":

                    Bank.data.remove(account)
                    Bank.update()

                    print("\n" + "=" * 50)
                    print("      ACCOUNT DELETED SUCCESSFULLY")
                    print("=" * 50)

                else:
                    print("\nAccount deletion cancelled.")

                return

        print("\nInvalid Account Number or PIN.")
         


# ---------------- MAIN PROGRAM ---------------- #

user = Bank()

print("\n========== BANK MANAGEMENT SYSTEM ==========\n")
print("1. Create Account")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. View Details")
print("5. Update Details")
print("6. Delete Account")

try:
    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        user.create_account()

    elif choice == 2:
        user.deposit_money()
    
    elif choice == 3:
        user.withdraw_money()

    elif choice == 4:
        user.view_details()

    elif choice == 5:
        user.update_details()

    elif choice == 6:
        user.delete_account()

    else:
        print("\n INVALID CHOICE .")

except ValueError:
    print("\nPlease enter a valid number.")