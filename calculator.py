def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiate")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice not in ("1", "2", "3", "4", "5"):
        print("Invalid input")
        return

    num1 = get_valid_number("Enter first number: ")
    num2 = get_valid_number("Enter second number: ")

    if choice == "1":
        print(f"Result: {add(num1, num2)}")
    elif choice == "2":
        print(f"Result: {subtract(num1, num2)}")
    elif choice == "3":
        print(f"Result: {multiply(num1, num2)}")
    elif choice == "4":
        print(f"Result: {divide(num1, num2)}")
    elif choice == "5":
        print(f"Result: {exponentiate(num1, num2)}")
