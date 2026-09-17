# Name: Nabulay, Gabriel Seth B.
# Grade and Section: 8-Adelfa

while True: # Loops program
    grade = int(input("Enter your grade: ")) # Inputs user's grade

    if 0 <= grade <= 100: # Checks if user's grade is in the range between 0 and 100
        print("Valid grade.") # Outputs this message if user's grade is in the range.
        break
    else:
        print("Invalid grade. Grade must be between 0 and 100.") # Outputs this message and makes user re-enter grade.