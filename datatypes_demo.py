# TASK 2: Variables, Data Types & Type Conversion

# Declaring variables of different data types
integer_var = 10            # int
float_var = 20.5            # float
string_var = "Python"       # string
boolean_var = True          # boolean

# Printing values and their data types
print("integer_var:", integer_var, "Type:", type(integer_var))
print("float_var:", float_var, "Type:", type(float_var))
print("string_var:", string_var, "Type:", type(string_var))
print("boolean_var:", boolean_var, "Type:", type(boolean_var))

# Performing arithmetic operations
print("\n--- Arithmetic Operations ---")
print("Addition:", integer_var + float_var)
print("Subtraction:", float_var - integer_var)
print("Multiplication:", integer_var * 2)
print("Division:", float_var / 2)

# Type conversion using user input
print("\n--- Type Conversion ---")
try:
    user_int = int(input("Enter an integer number: "))
    user_float = float(input("Enter a float number: "))

    print("Converted Integer:", user_int, "Type:", type(user_int))
    print("Converted Float:", user_float, "Type:", type(user_float))

except ValueError:
    print("Invalid input! Please enter numeric values only.")

# String and number concatenation
print("\n--- String & Number Concatenation ---")
age = 22
print("My age is " + str(age))

# Dynamic typing demonstration
print("\n--- Dynamic Typing ---")
dynamic_var = 100
print("Value:", dynamic_var, "Type:", type(dynamic_var))

dynamic_var = "Now I am a string"
print("Value:", dynamic_var, "Type:", type(dynamic_var))
