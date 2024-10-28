    def numerical_letter_grade(grades):
        letter_grade_dict = {
            4.0: 'A+',
            (3.7, 4.0): 'A',
            (3.3, 3.7): 'A-',
            (3.0, 3.3): 'B+',
            (2.7, 3.0): 'B',
            (2.3, 2.7): 'B-',
            (2.0, 2.3): 'C+',
            (1.7, 2.0): 'C',
            (1.3, 1.7): 'C-',
            (1.0, 1.3): 'D+',
            (0.7, 1.0): 'D',
            (0.0, 0.7): 'D-',
            0.0: 'E'
        }

        for gpa in grades:
            if gpa in letter_grade_dict:
                print(letter_grade_dict[gpa])
            else:
                print('E')

        return letter_grade_dict

numerical_letter_grade([4.0, 3, 1.7, 2, 3.5])



# Another approach
def numerical_letter_grade(grades):
    """
    This function will take a list of GPAs and print out the corresponding
    letter grade. If the GPA is out of the range of the table, it will print an E.
    """
    letter_grades = {
        'A+': (4.0, 5.0),
        'A': (3.7, 4.0),
        'A-': (3.3, 3.7),
        'B+': (3.0, 3.3),
        'B': (2.7, 3.0),
        'B-': (2.3, 2.7),
        'C+': (2.0, 2.3),
        'C': (1.7, 2.0),
        'C-': (1.3, 1.7),
        'D