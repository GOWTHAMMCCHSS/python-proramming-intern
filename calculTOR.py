# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y
print("\t\tSIMPLE CALCULATOR")
print("\t\t******************")
print("Select operation:")
print("IF YOU WANT TO ADDITION KINDLY ENTER(add)")
print("IF YOU WANT TO SUBTRATION KINDLY ENTER(sub)")
print("IF YOU WANT TO MULTIPLICATION KINDLY ENTER(mul)")
print("IF YOU WANT TO DIVIDE KINDLY ENTER(div)")

while True:
    # Take input from the user
    choice = input("Enter choice (add/sub/mul/div): ")

    # Check if choice is one of the four options
    if choice in ('add', 'sub', 'mul', 'div'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 'add':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == 'sub':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == 'mul':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == 'div':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # Ask the user if they want to continue
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
