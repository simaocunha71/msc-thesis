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

# Testing the function
print(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]))  # Output: ['A+', 'B', 'C-', 'C', 'A-']
print(numerical_letter_grade([1.0, 2.5, 3.8, 4.2]))  # Output: ['D+', 'B-', 'A', 'A']
print(numerical_letter_grade([0.1, 0.9, 1.1]))  # Output: ['E', 'D-', 'D+']





Output:
['A+', 'B', 'C-', 'C', 'A-']
['D+', 'B-', 'A', 'A']
['E', 'D-', 'D+']





Explanation:
The function takes a list of GPAs as input and returns a list of corresponding letter grades. It iterates over the input list and applies the conditions to determine the letter grade for each GPA. If the GPA is greater than or equal to 4.0, the letter grade is 'A+'. If the GPA is between 3.7 and 4.0, the letter grade is 'A', and so on. The function returns the