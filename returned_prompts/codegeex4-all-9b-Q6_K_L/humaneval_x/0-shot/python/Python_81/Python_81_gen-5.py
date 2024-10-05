def numerical_letter_grade(grades):
    def grade_equation(x):
        if x == 4.0:
            return 'A+'
        elif x > 3.7:
            return 'A'
        elif x > 3.3:
            return 'A-'
        elif x > 3.0:
            return 'B+'
        elif x > 2.7:
            return 'B'
        elif x > 2.3:
            return 'B-'
        elif x > 2.0:
            return 'C+'
        elif x > 1.7:
            return 'C'
        elif x > 1.3:
            return 'C-'
        elif x > 1.0:
            return 'D+'
        elif x > 0.7:
            return 'D'
        elif x > 0.0:
            return 'D-'
        elif x == 0.0:
            return 'E'
    return [grade_equation(x) for x in grades]

print(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]))