# Name: Nabulay, Gabriel Seth B.
# Grade and Section: 8-Adelfa

while True:
    try:
        student_score = int(input("\nEnter examination score: ")) # Inputs user's exam score
    except ValueError: # Checks if user inputted an integer
        print("Invalid input. Please enter a number.") # Outputs this message and makes user re-input
    else:
        if 0 <= student_score <= 100: # Checks if score is in the range of 0-100
            print("Valid Score.") # Outputs this message if input is valid
            break
        else:
            print("Invalid input. Please enter the score between 0-100.") # Outputs this message if score isn't in the range of 0-100