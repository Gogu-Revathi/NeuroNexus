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
