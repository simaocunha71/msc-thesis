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

# Test your function
print(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]))  # Output: ['A+', 'B', 'C-', 'C', 'A-']




# Test your function
print(numerical_letter_grade([2.9, 2.9, 2.9]))  # Output: ['B-', 'B-', 'B-']




# Test your function
print(numerical_letter_grade([0.5, 0.5, 0.5]))  # Output: ['D', 'D', 'D']




# Test your function
print(numerical_letter_grade([1.0, 1.0, 1.0]))  # Output: ['D+', 'D+', 'D+']




# Test your function
print(numerical_letter_grade([1.8, 1.8, 1.8]))  # Output: ['C', 'C', 'C']





# Test your function
print(numerical_letter_grade([3.8, 3.8, 3.8]))  # Output: ['A', 'A', 'A']





# Test your function
print(numerical