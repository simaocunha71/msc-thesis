
def numerical_letter_grade(grades):
    letter_grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E']
    return [letter_grades[int((g-1)/0.1)] for g in grades]
