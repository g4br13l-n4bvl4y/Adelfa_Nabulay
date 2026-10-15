# Nabulay, Gabriel Seth B.
# 8 - Adelfa

# Define the global variables in program.
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

# This function calculates the sum of numbers
def calculate_sum(a, b):
    return a + b # Returns the sum of numbers

# This function calculates the difference of numbers
def calculate_difference(a, b):
    return a - b # Returns the difference of numbers

# Outputs the result of called functions
print("\nSum:", calculate_sum(number_1, number_2))
print("Difference:", calculate_difference(number_1, number_2))