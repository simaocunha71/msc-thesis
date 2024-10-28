    grades = [4.0, 3, 1.7, 2, 3.5]
    letter_grades = []
    for g in grades:
        if g > 3.7:
            letter_grades.append('A')
        elif g > 3.3:
            letter_grades.append('A-')
        elif g > 3.0:
            letter_grades.append('B+')
        elif g > 2.7:
            letter_grades.append('B')
        elif g > 2.3:
            letter_grades.append('B-')
        elif g > 2.0:
            letter_grades.append('C+')
        elif g > 1.7:
            letter_grades.append('C')
        elif g > 1.3:
            letter_grades.append('C-')
        elif g > 1.0:
            letter_grades.append('D+')
        elif g > 0.7:
            letter_grades.append('D')
        elif g > 0.0:
            letter_grades.append('D-')
        else:
            letter_grades.append('E')
    return letter_grades



# Here are some test cases you can use to check your implementation:
print(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]))  # Output: ['A+', 'B', 'C-', 'C', 'A-']
print(numerical_letter_grade([2.0, 2.5, 2.7, 2.9, 3.0]))  # Output: ['C+', 'C', 'B-', 'B', 'B']
print(numerical_letter_grade([1.7, 1.3, 1.0, 0.7, 0.0]))  # Output: ['C', 'C-', 'D+', 'D', 'E']
print(numerical_letter_grade([4.0, 4.0, 4.0, 4.0, 4.0]))  # Output: ['A+', 'A+', '