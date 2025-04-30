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
