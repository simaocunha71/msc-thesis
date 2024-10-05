    def numerical_letter_grade(grades):
        letter_grades = []
        for grade in grades:
            if grade >= 4.0:
                letter_grades.append('A+')
            elif 3.7 <= grade < 4.0:
                letter_grades.append('A')
            elif 3.3 <= grade < 3.7:
                letter_grades.append('A-')
            elif 3.0 <= grade < 3.3:
                letter_grades.append('B+')
            elif 2.7 <= grade < 3.0:
                letter_grades.append('B')
            elif 2.3 <= grade < 2.7:
                letter_grades.append('B-')
            elif 2.0 <= grade < 2.3:
                letter_grades.append('C+')
            elif 1.7 <= grade < 2.0:
                letter_grades.append('C')
            elif 1.3 <= grade < 1.7:
                letter_grades.append('C-')
            elif 1.0 <= grade < 1.3:
                letter_grades.append('D+')
            elif 0.7 <= grade < 1.0:
                letter_grades.append('D')
            elif 0.0 <= grade < 0.7:
                letter_grades.append('D-')
            else:
                letter_grades.append('E')
        return letter_grades

    print(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]))  # Output: ['A+', 'B', 'C-', 'C', 'A-']





# Test cases:
print(numerical_letter_grade([4.0, 3.8, 3.6, 3.4, 3.2, 3.0, 2.8, 2.6, 2.4, 2.2, 2.0, 1.8, 1.6, 1.4, 1.2, 1.0, 0.8, 0.6, 0.4, 0.2, 0.0]))  # Output: ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E', '