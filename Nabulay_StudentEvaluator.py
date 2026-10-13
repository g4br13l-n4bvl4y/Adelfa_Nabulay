# Nabulay, Gabriel Seth B.
# 8 - Adelfa

student_name = ""
score1 = 0
score2 = 0
score3 = 0
avg = 0
performance_level = ""

def display_header():
    print("STUDENT PERFORMANCE EVALUATOR")

def get_student_info():
    global student_name, score1, score2, score3

    student_name = input("Enter student name: ")
    score1 = int(input("Enter Assessment 1: "))
    score2 = int(input("Enter Assessment 2: "))
    score3 = int(input("Enter Assessment 3: "))

def evaluate_performance(score1, score2, score3):
    global avg, performance_level

    avg = (score1 + score2 + score3) / 3

    if avg >= 90:
        performance_level = "Outstanding"
    elif avg >= 85:
        performance_level = "Very Satisfactory"
    elif avg >= 80:
        performance_level = "Satisfactory"
    elif avg >= 75:
        performance_level = "Fairly Satisfactory"
    else:
        performance_level = "Needs Improvement"

def display_report():
    print("\nSTUDENT PERFORMANCE REPORT")
    print(f"Student Name: {student_name}")
    print(f"Assessment Scores: {score1}, {score2}, {score3}")
    print(f"Average Score: {avg:.2f}")
    print(f"Performance Level: {performance_level}")

display_header()
get_student_info()
evaluate_performance(score1, score2, score3)
display_report()
