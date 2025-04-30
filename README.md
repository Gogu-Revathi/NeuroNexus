
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

