AIRTEL MONEY SIMULATION SYSTEM

Course: ICT111 – Principles of Programming (Python & Git)
Institution: Mulungushi University
Department: Computer Science and Information Technology

1. Project Overview

The Airtel Money Simulation System is a Python-based, menu-driven application that simulates basic mobile money services. It allows users to register an account, check balances, deposit money, send money, withdraw money and manage account details.

The project demonstrates practical applications of basic Python programming concepts.

Note: This is an educational simulation. It does not connect to the real Airtel Money network or process actual payments.

2. Main Features

The application provides the following services:

1. Account Registration: Creates a customer account using a name, phone number, NRC and four-digit PIN.
2. Check Balance: Displays the customer's available balance after PIN verification.
3. Send Money: Transfers simulated money to another valid phone number.
4. Deposit Money: Adds money to the account balance.
5. Withdraw Money: Deducts money from the available balance.
6. Edit Account Details: Allows customers to update their name or phone number.
7. Account Details: Displays customer information without revealing the PIN.
8. Transaction History: Shows successful deposits, transfers and withdrawals.
9. Change PIN: Allows customers to change their existing PIN.
10. Exit: Closes the application.

3. Python Concepts Used

The project demonstrates:

- Variables and data types.
- User input and output.
- Arithmetic operations.
- Conditional statements ("if", "elif", "else").
- Loops ("while" and "for").
- Functions for organising code.
- Input validation and error handling.
- Formatted strings (f-strings).

4. Requirements

To run the application, you need:

- Python 3 installed.
- Visual Studio Code or another Python editor.
- A computer terminal or command prompt.

No additional Python packages are required.

5. How to Run the Program

1. Open the project folder in Visual Studio Code.

2. Open the terminal.

3. Check that Python is installed:
   
   "python --version"

4. Run the application:
   
   "python airtel_money.py"

5. Follow the menu instructions and enter the number corresponding to your preferred service.

Enter "0" to exit.

6. Security and Validation

The application includes basic validation to improve accuracy and protect account operations.

- Phone numbers must contain 10 digits and start with 097 or 077.
- PINs must contain exactly four digits.
- Transaction amounts must be positive.
- Transfers and withdrawals cannot exceed the available balance.
- PIN verification is required for protected operations.
- Users cannot send money to their own number.
- Invalid inputs are rejected.

7. Git Version Control

Git is used to track changes and manage project development.

Important commands:

- "git init" – Creates a Git repository.
- "git add ." – Adds project files.
- "git commit -m "message"" – Saves project changes.
- "git log --oneline" – Displays commit history.
- "git status" – Checks repository status.

At least three meaningful commits should be made during development.

8. Project Limitations

- The application operates through a command-line interface.
- Account information is stored temporarily in program memory.
- Data is lost when the application closes.
- It does not connect to real Airtel Money services.
- All financial transactions are simulated.

9. Conclusion

The Airtel Money Simulation System demonstrates how Python programming can be used to develop a simple mobile money application. It combines account management, transaction processing, input validation and Git version control into one practical academic project.

Important: Use dummy customer information and a dummy PIN only. This is not an official Airtel Money application.