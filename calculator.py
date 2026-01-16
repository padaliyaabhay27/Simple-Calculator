# Simple Calculator Program with input validation

def get_number(prompt):
    while True:
        user_input = input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input! Please enter a number.")

# Get valid numbers from the user
a = get_number("Enter first number: ")
b = get_number("Enter second number: ")

# Perform calculations
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b != 0:
    print("Division:", a / b)
else:
    print("Division not possible")