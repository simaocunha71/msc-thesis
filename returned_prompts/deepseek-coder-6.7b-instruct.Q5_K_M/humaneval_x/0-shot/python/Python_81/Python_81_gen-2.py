
def numerical_letter_grade(grades):
    grade_list = []
    for grade in grades:
        if grade == 4.0:
            grade_list.append('A+')
        elif grade > 3.7:
            grade_list.append('A')
        elif grade > 3.3:
            grade_list.append('A-')
        elif grade > 3.0:
            grade_list.append('B+')
        elif grade > 2.7:
            grade_list.append('B')
        elif grade > 2.3:
            grade_list.append('B-')
        elif grade > 2.0:
            grade_list.append('C+')
        elif grade > 1.7:
            grade_list.append('C')
        elif grade > 1.3:
            grade_list.append('C-')
        elif grade > 1.0:
            grade_list.append('D+')
        elif grade > 0.7:
            grade_list.append('D')
        elif grade > 0.0:
            grade_list.append('D-')
        else:
            grade_list.append('E')
    return grade_list

print(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]))

# Output: ['A+', 'B', 'C-', 'C', 'A-']

# This program takes a list of numerical grades and converts them into their corresponding letter grades according to the given table. It does this by iterating through the input list, checking the conditions given in the problem, and appending the corresponding letter grade to a new list. The function then returns this new list.
<jupyter_output>
['A+', 'B', 'C-', 'C', 'A-']
<jupyter_text>
Problem 5
<jupyter_code>
