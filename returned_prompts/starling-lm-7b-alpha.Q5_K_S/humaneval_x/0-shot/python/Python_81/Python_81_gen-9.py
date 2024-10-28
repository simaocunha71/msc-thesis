    grades = [4.0, 3, 1.7, 2, 3.5]

    grades_list = []

    for gpa in grades:
        if gpa > 3.7:
            grades_list.append('A+')
        elif gpa > 3.3:
            grades_list.append('A')
        elif gpa > 3.0:
            grades_list.append('A-')
        elif gpa > 2.7:
            grades_list.append('B+')
        elif gpa > 2.3:
            grades_list.append('B')
        elif gpa > 2.0:
            grades_list.append('B-')
        elif gpa > 1.7:
            grades_list.append('C+')
        elif gpa > 1.3:
            grades_list.append('C')
        elif gpa > 1.0:
            grades_list.append('C-')
        elif gpa > 0.7:
            grades_list.append('D+')
        elif gpa > 0.0:
            grades_list.append('D')
        elif gpa > -0.0:
            grades_list.append('D-')
        else:
            grades_list.append('E')
    return grades_list


# Here is a test case to check your code:
# If all the tests pass, it will print "All tests passed."
def test():
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']
    assert numerical_letter_grade([3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0, -0.0]) == ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D',