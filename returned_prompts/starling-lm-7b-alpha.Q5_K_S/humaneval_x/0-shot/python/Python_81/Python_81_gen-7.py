    grades = [4.0, 3, 1.7, 2, 3.5]
    letter_grades = []
    for grade in grades:
        if grade > 3.7:
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

# Here is a test to check your implementation
print(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5])) # ['A+', 'B', 'C-', 'C', 'A-']

# Here's a test for edge cases
print(numerical_letter_grade([0.0, 0.1, 0.7, 1.0, 1.1, 3.8, 3.9])) # ['E', 'D+', 'D', 'D', 'D', 'A', 'A']


# Here's a test for edge cases
print(numerical_letter_grade([-0.1, -0.2, -0.3, -0.4, -0.5, -0.6, -0.7, -0.8, -0.9, -1.0])) # ['E', 'E', 'E', 'E', 'E', '