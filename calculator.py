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

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator!"

print("Result:", result)