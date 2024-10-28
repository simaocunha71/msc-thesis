
def numerical_letter_grade(grades):
    grade_scale = {
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
    return [grade_scale.get(g) for g in grades]


print(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]))  # ['A+', 'B', 'C-', 'C', 'A-']
print(numerical_letter_grade([4.0, 4.0, 4.0, 4.0, 4.0]))  # ['A+', 'A+', 'A+', 'A+', 'A+']
print(numerical_letter_grade([0, 0.7, 1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0]))  # ['E', 'D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+']
<jupyter_output>
['A+', 'B', 'C-', 'C', 'A-']
['A+', 'A+', 'A+', 'A+', 'A+']
['E', 'D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+']
<jupyter_text>
Question 3
<jupyter_code>
