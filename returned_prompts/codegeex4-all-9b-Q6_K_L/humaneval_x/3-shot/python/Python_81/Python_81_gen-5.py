    grade_table = {
        (4.0, float('inf')): 'A+',
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
        (float('-inf'), 0.0): 'E'
    }

    return [grade_table[(lower_bound, upper_bound)] for lower_bound, upper_bound in grade_table.keys() if lower_bound <= grade <= upper_bound for grade in grades]