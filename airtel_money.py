"""
Airtel Money Simulation System
ICT111 - Principles of Programming (Python & Git)
For learning only: uses simulated customer information and no real money.
"""

account = None
balance = 0.00
transactions = []


def valid_phone(phone):
    return (
        len(phone) == 10
        and phone.isdigit()
        and (phone.startswith("097") or phone.startswith("077"))
    )


def get_positive_amount(prompt):
    while True:
        raw_amount = input(prompt).strip()
        try:
            amount = float(raw_amount)
            if amount <= 0:
                print("Amount must be greater than K0.00.")
            else:
                return round(amount, 2)
        except ValueError:
            print("Invalid amount. Enter numbers only, for example 50 or 50.50.")


def verify_pin():
    entered_pin = input("Enter your 4-digit PIN: ").strip()
    if entered_pin == account["pin"]:
        return True
    print("Incorrect PIN. Access denied.")
    return False


def register_account():
    global account, balance

    if account is not None:
        print("An account is already registered on this simulation.")
        return

    print("\n--- REGISTER ACCOUNT ---")
    while True:
        name = input("Enter full name: ").strip()
        if name:
            break
        print("Name cannot be empty.")

    while True:
        phone = input("Enter 10-digit phone number (097/077): ").strip()
        if valid_phone(phone):
            break
        print("Invalid phone number. It must have 10 digits and start with 097 or 077.")

    while True:
        nrc = input("Enter a DUMMY NRC number: ").strip()
        if nrc:
            break
        print("NRC cannot be empty.")

    while True:
        pin = input("Create a 4-digit dummy PIN: ").strip()
        if len(pin) == 4 and pin.isdigit():
            break
        print("PIN must contain exactly four digits.")

    account = {"name": name, "phone": phone, "nrc": nrc, "pin": pin}
    balance = 0.00
    print("\nAccount registered successfully!")
    print("Opening balance: K0.00")


def check_balance():
    if account is None:
        print("Please register an account first.")
    elif verify_pin():
        print(f"Account holder: {account['name']}")
        print(f"Available balance: K{balance:.2f}")


def send_money():
    global balance

    if account is None:
        print("Please register an account first.")
        return

    print("\n--- SEND MONEY ---")
    recipient = input("Enter recipient's 10-digit Airtel number: ").strip()

    if not valid_phone(recipient):
        print("Invalid recipient number.")
        return
    if recipient == account["phone"]:
        print("You cannot send money to your own number.")
        return

    amount = get_positive_amount("Enter amount to send (K): ")
    if amount > balance:
        print("Transaction rejected: insufficient funds.")
        return
    if not verify_pin():
        return

    balance = round(balance - amount, 2)
    transactions.append(
        f"Sent K{amount:.2f} to {recipient}. Balance: K{balance:.2f}"
    )
    print(f"Successfully sent K{amount:.2f} to {recipient}.")
    print(f"New balance: K{balance:.2f}")


def deposit_money():
    global balance

    if account is None:
        print("Please register an account first.")
        return

    print("\n--- DEPOSIT MONEY ---")
    amount = get_positive_amount("Enter amount to deposit (K): ")
    balance = round(balance + amount, 2)
    transactions.append(f"Deposited K{amount:.2f}. Balance: K{balance:.2f}")
    print(f"Deposit successful. New balance: K{balance:.2f}")


def withdraw_money():
    global balance

    if account is None:
        print("Please register an account first.")
        return

    print("\n--- WITHDRAW MONEY ---")
    amount = get_positive_amount("Enter amount to withdraw (K): ")
    if amount > balance:
        print("Withdrawal rejected: insufficient funds.")
        return
    if not verify_pin():
        return

    balance = round(balance - amount, 2)
    transactions.append(f"Withdrew K{amount:.2f}. Balance: K{balance:.2f}")
    print(f"Withdrawal successful. New balance: K{balance:.2f}")


def edit_details():
    if account is None:
        print("Please register an account first.")
        return

    print("\n--- EDIT USER DETAILS ---")
    if not verify_pin():
        return

    print("1. Edit name")
    print("2. Edit phone number")
    choice = input("Choose what to edit: ").strip()

    if choice == "1":
        while True:
            new_name = input("Enter new full name: ").strip()
            if new_name:
                account["name"] = new_name
                print("Name updated successfully.")
                break
            print("Name cannot be empty.")
    elif choice == "2":
        while True:
            new_phone = input("Enter new 10-digit phone (097/077): ").strip()
            if valid_phone(new_phone):
                account["phone"] = new_phone
                print("Phone number updated successfully.")
                break
            print("Invalid phone number.")
    else:
        print("Invalid choice. No details were changed.")


def view_account_details():
    if account is None:
        print("No account is registered.")
        return

    masked_nrc = "*" * max(0, len(account["nrc"]) - 3) + account["nrc"][-3:]
    print("\n--- ACCOUNT DETAILS ---")
    print(f"Name: {account['name']}")
    print(f"Phone: {account['phone']}")
    print(f"NRC: {masked_nrc}")
    print("Registration status: Registered")
    print("PIN: Hidden")


def transaction_history():
    if account is None:
        print("Please register an account first.")
    elif not transactions:
        print("No transactions have been made yet.")
    else:
        print("\n--- TRANSACTION HISTORY ---")
        for number, transaction in enumerate(transactions, start=1):
            print(f"{number}. {transaction}")


def change_pin():
    if account is None:
        print("Please register an account first.")
        return

    print("\n--- CHANGE PIN ---")
    if not verify_pin():
        return

    while True:
        new_pin = input("Enter a new 4-digit PIN: ").strip()
        if len(new_pin) != 4 or not new_pin.isdigit():
            print("PIN must contain exactly four digits.")
        elif new_pin == account["pin"]:
            print("The new PIN must be different from the old PIN.")
        else:
            account["pin"] = new_pin
            print("PIN changed successfully.")
            break


def main():
    while True:
        print("\n========== AIRTEL MONEY ==========")
        print("1. Register Account")
        print("2. Check Balance")
        print("3. Send Money")
        print("4. Deposit Money")
        print("5. Withdraw Money")
        print("6. Edit Details")
        print("7. Account Details")
        print("8. Transaction History")
        print("9. Change PIN")
        print("0. Exit")
        print("==================================")

        choice = input("Select an option: ").strip()

        if choice == "1":
            register_account()
        elif choice == "2":
            check_balance()
        elif choice == "3":
            send_money()
        elif choice == "4":
            deposit_money()
        elif choice == "5":
            withdraw_money()
        elif choice == "6":
            edit_details()
        elif choice == "7":
            view_account_details()
        elif choice == "8":
            transaction_history()
        elif choice == "9":
            change_pin()
        elif choice == "0":
            print("Thank you for using Airtel Money Simulation. Goodbye!")
            break
        else:
            print("Invalid menu choice. Please select an option from 0 to 9.")


if __name__ == "__main__":
    main()