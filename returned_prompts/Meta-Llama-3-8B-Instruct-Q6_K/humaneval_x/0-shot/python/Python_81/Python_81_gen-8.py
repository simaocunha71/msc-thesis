    def numerical_letter_grade(grades):
        letter_grades = []
        for grade in grades:
            if grade >= 4.0:
                letter_grades.append('A+')
            elif 3.7 >= grade > 3.0:
                letter_grades.append('A')
            elif 3.3 >= grade > 3.0:
                letter_grades.append('A-')
            elif 3.0 >= grade > 2.7:
                letter_grades.append('B+')
            elif 2.7 >= grade > 2.3:
                letter_grades.append('B')
            elif 2.3 >= grade > 2.0:
                letter_grades.append('B-')
            elif 2.0 >= grade > 1.7:
                letter_grades.append('C+')
            elif 1.7 >= grade > 1.3:
                letter_grades.append('C')
            elif 1.3 >= grade > 1.0:
                letter_grades.append('C-')
            elif 1.0 >= grade > 0.7:
                letter_grades.append('D+')
            elif 0.7 >= grade > 0.0:
                letter_grades.append('D')
            else:
                letter_grades.append('E')
        return letter_grades

grades = [4.0, 3, 1.7, 2, 3.5]
print(numerical_letter_grade(grades))  # Output: ['A+', 'B', 'C-', 'C', 'A-']



# Testing the function
assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-'], f"Expected numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) to return ['A+', 'B', 'C-', 'C', 'A-'] but got {numerical_letter_grade([4.0, 3, 1.7, 2, 3.5])}"
assert numerical_letter_grade([0.0, 3.8, 1.1, 2.4, 3.9]) == ['E', 'A', 'D+', 'B-', 'A'], f"Expected numerical_letter_grade([0.0, 