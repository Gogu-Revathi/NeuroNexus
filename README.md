# NeuroNexus

Skip to content
Navigation Menu
Gogu-Revathi
NeuroNexus

Type / to search
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
Commit 99efab7
Gogu-Revathi
Gogu-Revathi
authored
now
Verified
Add files via upload
Task 1: Advanced Calculator with Historical Functionality**

Description:

This is an advanced calculator application that enables users to carry out various mathematical operations like addition, subtraction, multiplication, division, exponentiation, and modulus. It also features a past calculations storage for future reference. Users can opt to use numeric values or even calculate mathematical expressions.

Characteristics:

1. Basic Mathematical Operations: Carry out arithmetic operations between two or more numbers like addition, subtraction, multiplication, division, exponentiation, and modulus.
2. Expression Evaluation: Allows the user to directly evaluate mathematical expressions (e.g., `55 * 3 + (657 - 748) % 78`).
3. History: The program keeps track of the calculations made during the session, hence allowing users to access previous calculations.
4. Error Handling* The application deals with invalid inputs such as non-numeric inputs and division by zero situations graciously.
5. User Interaction: A simple text-menu designed to encourage users to choose operations and inspect results.

Instructions for Use:
- Choose from operation type (expression or numbers).
- Enter the desired expression or operation.
The result is presented and recorded in the history.
At any time during the session, one can refer to earlier calculations.

---



Task 2: Advanced Password Generator

Description:

This is a password generator tool that enables the user to generate strong, customized passwords according to his or her own requirements. The user can choose the characters to be used (uppercase, lower case, numbers, symbols) and at what length the password should be. The password is then printed and copied to the clipboard, if the `pyperclip` package is installed, for ease of use.

Characteristics:
1. Password Length: Asks the user to specify the desired length for the password to be generated.
2. Choice of Character Type: This option enables the user to choose whether to include uppercase letters, lowercase letters, numbers, and symbols in the password.
3. Password Generation: Randomly generates a password according to the user's requirements.
4. Clipboard Copy: The generated password can be copied to the clipboard for easy use if `pyperclip` exists. If `pyperclip` does not exist, a notice to install will be shown.
5. Error Handling: The application addresses invalid inputs (for instance, inputting a non-integer for password length) and requests the user to reenter them.

Method of Utilization:

- Define the password length to be wished (minimum of 4 characters).

- Select which types of characters (uppercase, lowercase, numbers, symbols) to add to the password. - It prints the password and, if `pyperclip` is installed, copies the password to the clipboard.
These definitions set the functionality and purpose of the two work items. You can feel free to extend or alter them according to any other features or data you want to highlight.
main
1 parent 
f27e5a5
 commit 
99efab7
File tree
Filter files…
calculator.py
password_generator.py
2 files changed
+132
-0
lines changed
Search within code
 
‎calculator.py
+89
Original file line number	Diff line number	Diff line change
@@ -0,0 +1,89 @@
def calculator():
    print("Calculator")
    print("----------")
    history = []
    while True:
        print("\nChoose an option:")
        print(" 1. Evaluate Expression")
        print(" 2. Perform Operations with Numbers ")
        print(" 3. View History")
        print(" 4. Quit")
        choice = input("Enter option (1/2/3/4): ").strip()
        if choice == '4':
            print("Exiting calculator. Goodbye!")
            break
        elif choice == '3':
            if history:
                print("\nCalculation History:")
                for record in history:
                    print(record)
            else:
                print("No calculations yet.")
            continue
        elif choice == '1':
            expression = input("Enter the expression to evaluate (e.g. 55 * 3 + (657 - 748) % 78): ").strip()
            try:
                result = eval(expression)
                print("Result:", result)
                history.append(f"{expression} = {result}")
            except Exception as e:
                print(f"Error evaluating expression: {e}")
            continue
        elif choice == '2':
            try:
                num_count = int(input("How many numbers do you want to perform operations on? "))
                numbers = []
                for i in range(num_count):
                    num = float(input(f"Enter number {i+1}: "))
                    numbers.append(num)
                print("\nChoose an operation:")
                print(" +  Addition")
                print(" -  Subtraction")
                print(" *  Multiplication")
                print(" /  Division")
                print(" ^  Power")
                print(" %  Modulus")
                operation = input("Enter operator: ").strip()
                if operation == '+':
                    result = sum(numbers)
                elif operation == '-':
                    result = numbers[0]
                    for num in numbers[1:]:
                        result -= num
                elif operation == '*':
                    result = 1
                    for num in numbers:
                        result *= num
                elif operation == '/':
                    result = numbers[0]
                    for num in numbers[1:]:
                        if num == 0:
                            print("Error: Division by zero!")
                            break
                        result /= num
                elif operation == '^':
                    result = numbers[0]
                    for num in numbers[1:]:
                        result **= num
                elif operation == '%':
                    result = numbers[0]
                    for num in numbers[1:]:
                        result %= num
                else:
                    print("Invalid operation.")
                    continue
                print("Result:", result)
                history.append(f"Operation on {numbers} with '{operation}' = {result}")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
            except Exception as e:
                print(f"Error: {e}")
            continue
        else:
            print("Invalid option. Please choose again.")
calculator()
‎password_generator.py
+43
Original file line number	Diff line number	Diff line change
@@ -0,0 +1,43 @@
import random
import string
try:
    import pyperclip
except ImportError:
    pyperclip = None  
def generate_password():
    print("Advanced Password Generator")
    print("---------------------------")
    try:
        length = int(input("Enter desired password length: "))
        if length < 4:
            print("Password length should be at least 4.")
            return
        include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        include_digits = input("Include numbers? (y/n): ").lower() == 'y'
        include_symbols = input("Include symbols? (e.g., @#$%) (y/n): ").lower() == 'y'
        characters = ''
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_lowercase:
            characters += string.ascii_lowercase
        if include_digits:
            characters += string.digits
        if include_symbols:
            characters += string.punctuation
        if not characters:
            print("You must select at least one character type.")
            return
        password = ''.join(random.choice(characters) for _ in range(length))
        print(f"\nGenerated Password: {password}")
        if pyperclip:
            pyperclip.copy(password)
            print("Password copied to clipboard!")
        else:
            print("(Tip: install 'pyperclip' module to enable clipboard copy)")
    except ValueError:
        print(" Please enter a valid number for length.")
generate_password()
0 commit comments
Comments
0
 (0)
Comment
You're receiving notifications because you're subscribed to this thread.

Add files via upload · Gogu-Revathi/NeuroNexus@99efab7
