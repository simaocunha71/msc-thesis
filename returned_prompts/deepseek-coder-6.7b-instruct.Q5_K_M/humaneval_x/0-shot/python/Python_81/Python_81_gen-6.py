
    def numerical_letter_grade(grades):
        letter_grades = []
        for grade in grades:
            if grade == 4.0:
                letter_grades.append("A+")
            elif grade > 3.7:
                letter_grades.append("A")
            elif grade > 3.3:
                letter_grades.append("A-")
            elif grade > 3.0:
                letter_grades.append("B+")
            elif grade > 2.7:
                letter_grades.append("B")
            elif grade > 2.3:
                letter_grades.append("B-")
            elif grade > 2.0:
                letter_grades.append("C+")
            elif grade > 1.7:
                letter_grades.append("C")
            elif grade > 1.3:
                letter_grades.append("C-")
            elif grade > 1.0:
                letter_grades.append("D+")
            elif grade > 0.7:
                letter_grades.append("D")
            elif grade > 0.0:
                letter_grades.append("D-")
            else:
                letter_grades.append("E")
        return letter_grades

    print(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]))  # ['A+', 'B', 'C-', 'C', 'A-']

    # Alternative solution with list comprehension:

    def numerical_letter_grade(grades):
        return ['A+' if grade == 4.0 else 'A' if grade > 3.7 else 'A-' if grade > 3.3 else 'B+' if grade > 3.0 else 'B' if grade > 2.7 else 'B-' if grade > 2.3 else 'C+' if grade > 2.0 else 'C' if grade > 1.7 else 'C-' if grade > 1.3 else 'D+' if grade > 1.0 else 'D' if grade > 0.7 else 'D-' if grade > 0.0 else 'E' for grade in grades]

    print(numerical_letter_grade([4.0,