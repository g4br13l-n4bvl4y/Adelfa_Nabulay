# Name: Nabulay, Gabriel Seth B.
# Grade and Section: 8-Adelfa

import re

while True:
    student_ID = input("\nEnter Student ID: ")

    if re.fullmatch(r"\d{4}-\d{4}", student_ID):
        print("Valid Student ID.")
    else:
        print("Invalid Student ID.")