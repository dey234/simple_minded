# Simple calculator program
# Algorithm:
# 1. Ask the user for the first number.
# 2. Ask the user for an operator (+, -, *, /).
# 3. Ask the user for the second number.
# 4. Check which operator was entered.
# 5. Perform that operation on the two numbers.
# 6. If the operator is / and the second number is 0, show an error instead of dividing.
# 7. If the operator isn't one of the four, show an error message.
# 8. Print the result.

# Read the first number from the user so the calculation has a starting value.
num1 = float(input("Enter first number: "))

# Read the arithmetic symbol chosen by the user to decide what to calculate.
operator = input("Enter operator (+, -, *, /): ")

# Read the second number from the user to complete the operation.
num2 = float(input("Enter second number: "))

# Choose the correct math operation based on the symbol entered by the user.
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    # Prevent division by zero and show a clear error message instead.
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    # Handle invalid operator input.
    result = "Invalid operator!"

# Display the final answer in the terminal.
print("Result:", result)