# This contains some basic variable assignments and operations in Python.
# Each section will be separated by comments for clarity.
# Turn sections of practice into comments after you finish them by blocking then press 
# Ctrl + / (on Windows) or Command + / (on Mac).

# Concepts: int, float, str, bool, None, type(), type conversion, naming rules.

print("SECTION 1") 
# 🟢 Create variables for your name, age, height, and whether you are a student. 
# Print each one with its type().

name = "Aldelia"
age = 24
height = 150.5
is_student = False

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))
print()

print("SECTION 2") 
# 🟢 Swap two variables a and b using a third variable. 
# Then do it again in one line with a, b = b, a.

a = 1
b = 2
c = a  # Store the value of a in a temporary variable
a = b  # a becomes 2
b = c  # b becomes 1

print(a, b)  # Output: 2 1

a, b = b, a  # Swap in one line
print(a, b)  # Output: 1 2
print()

print("SECTION 3") 
# 🟢 Convert the string "42" to an int, add 8, and print the result. 
# Then convert it back to a string and join it with " apples".

str_to_num = int("42")
result = str_to_num + 8
print(result)  # Output: 50

str_result = str(result)
print(str_result + " apples")  # Output: 50 apples
print()

print("SECTION 4") 
# 🟢 Predict, then check: int(3.9), float("2.5"), bool(0), bool(""), bool("False"), str(True).

print(int(3.9))  # Prediction: 3 , returns only the integer part and ignore the rest.
print(float("2.5"))  # Prediction: 2.5 , returns the string as a float value.
print(bool(0))  # Prediction: False , because boolean treats numeric 0 as falsy and nonzero as truthy.
# Means bool(1) or bool(-1) would be True.
print(bool(""))  # Prediction: False , because boolean sees empty string as falsy and non-empty one as truthy.
print(bool("False"))  # Prediction: False, Output: True , because booleam sees this as a non-empty string.
print(str(True))  # Prediction: True , returns the argument inside the parentheses as a string.
print()

print("SECTION 5") 
# 🟡 Write a program that stores a temperature in Celsius and prints Fahrenheit using F = C * 9/5 + 32. 
# Format the output to 1 decimal place.

# celcius = float(input("Input the temperature in Celcius: "))
# fahrenheit = celcius * 9/5 + 32

# print(f"{fahrenheit:.1f} °F")
# print()

print("SECTION 6")
# 🟡 Find out what happens with 0.1 + 0.2 == 0.3. 
# Explain why, then fix the comparison using round() or abs(a - b) < 1e-9.

print(0.1 + 0.2 == 0.3)  # Output: False , why? 
# Because computers store many decimal fractions as close binary approximations, so 0.1 + 0.2 becomes approximately 0.30000000000000004.
print(round(0.1 + 0.2) == round(0.3))  # Output: True
print(abs((0.1 + 0.2) - 0.3) < 1e-9) # Output: True ,  this checks whether the difference is tiny enough to count as equal. 
# Because it's True, means the difference between the two numbers is smaller than 0.000000001, so we treat them as equal for this comparison.
print(round(0.1 + 0.2, 10) == round(0.3, 10))  # Output: True , meaning that both values become equal when rounded to 10 decimal places. 

print("SECTION 7")
# 🟡 Try int("abc") and int("3.5") and read both errors. 
# Write down in a comment what each error name means.

