# Nabulay, Gabriel Seth B.
# 8 - Adelfa

# Define the global variables in program.
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

# This function calculates the sum of numbers and outputs it
def calculate_sum(a, b): # a & b are local variables
    print(f"Sum: {a + b}") # Returns the sum of numbers

# This function calculates the difference of numbers and outputs it
def calculate_difference(a, b): # a & b are local variables
    print(f"Difference: {a - b}") # Returns the difference of numbers

# Functions are called
calculate_sum(number_1, number_2)
calculate_difference(number_1, number_2)