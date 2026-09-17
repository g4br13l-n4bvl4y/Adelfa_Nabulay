# Name: Nabulay, Gabriel Seth B.
# Grade and Section: 8-Adelfa

import re # Imports RegEx

while True:
    student_ID = input("\nEnter Student ID: ") # Inputs user's student ID

    if re.fullmatch(r"\d{4}-\d{4}", student_ID): # Checks if student ID's pattern follows this pattern (4 digits - 4 digits)
        print("Valid Student ID.") # Outputs this message if student ID pattern is valid.
        break
    else:
        print("Invalid Student ID.") # Outputs this message if student ID pattern is invalid and makes user re-input