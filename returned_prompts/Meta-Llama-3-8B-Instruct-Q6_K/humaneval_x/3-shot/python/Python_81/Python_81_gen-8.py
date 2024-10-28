    def numerical_letter_grade(grades):
        letter_grades = []
        for grade in grades:
            if grade >= 4.0:
                letter_grades.append('A+')
            elif grade > 3.7:
                letter_grades.append('A')
            elif grade > 3.3:
                letter_grades.append('A-')
            elif grade > 3.0:
                letter_grades.append('B+')
            elif grade > 2.7:
                letter_grades.append('B')
            elif grade > 2.3:
                letter_grades.append('B-')
            elif grade > 2.0:
                letter_grades.append('C+')
            elif grade > 1.7:
                letter_grades.append('C')
            elif grade > 1.3:
                letter_grades.append('C-')
            elif grade > 1.0:
                letter_grades.append('D+')
            elif grade > 0.7:
                letter_grades.append('D')
            elif grade > 0.0:
                letter_grades.append('D-')
            else:
                letter_grades.append('E')
        return letter_grades

    print(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]))  # Output: ['A+', 'B', 'C-', 'C', 'A-']  # Example output
#   print(numerical_letter_grade([3.9, 2.9, 3.1, 3.5, 2.6])) # Example output: ['A+', 'B-', 'B+', 'A-', 'B-']
#   print(numerical_letter_grade([1.0, 1.2, 1.9, 2.3, 3.4])) # Example output: ['D+', 'D+', 'C+', 'B-', 'A-']  # Example output
#   print(numerical_letter_grade([2.5, 3.0, 3.5, 4.0, 4.1])) # Example output: ['B-', 'B+', 'A-', 'A+', 'A+']  # Example output
#   print(numerical_letter_grade([1.1, 1.4, 1.7, 2.0, 2.3])) # Example output: ['D+', '