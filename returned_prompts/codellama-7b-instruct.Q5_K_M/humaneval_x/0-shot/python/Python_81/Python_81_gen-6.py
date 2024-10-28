
def numerical_letter_grade(grades):
    letter_grade_list = []
    for grade in grades:
        if grade >= 4.0:
            letter_grade = 'A+'
        elif grade > 3.7:
            letter_grade = 'A'
        elif grade > 3.3:
            letter_grade = 'A-'
        elif grade > 3.0:
            letter_grade = 'B+'
        elif grade > 2.7:
            letter_grade = 'B'
        elif grade > 2.3:
            letter_grade = 'B-'
        elif grade > 2.0:
            letter_grade = 'C+'
        elif grade > 1.7:
            letter_grade = 'C'
        elif grade > 1.3:
            letter_grade = 'C-'
        elif grade > 1.0:
            letter_grade = 'D+'
        elif grade > 0.7:
            letter_grade = 'D'
        elif grade > 0.0:
            letter_grade = 'D-'
        else:
            letter_grade = 'E'
        letter_grade_list.append(letter_grade)
    return letter_grade_list

B:

def numerical_letter_grade(grades):
    grade_dict = {
        4.0: 'A+',
        3.7: 'A',
        3.3: 'A-',
        3.0: 'B+',
        2.7: 'B',
        2.3: 'B-',
        2.0: 'C+',
        1.7: 'C',
        1.3: 'C-',
        1.0: 'D+',
        0.7: 'D',
        0.0: 'D-',
        0.0: 'E'
    }
    return [grade_dict[grade] for grade in grades]

C:

def numerical_letter_grade(grades):
    grade_dict = {
        4: 'A',
        3: 'A',
        3: 'A',
        3: 'A