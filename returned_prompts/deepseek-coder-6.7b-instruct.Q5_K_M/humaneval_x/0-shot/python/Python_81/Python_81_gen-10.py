
def numerical_letter_grade(grades):
    grades_list = []
    for g in grades:
        if g == 4.0:
            grades_list.append('A+')
        elif g > 3.7:
            grades_list.append('A')
        elif g > 3.3:
            grades_list.append('A-')
        elif g > 3.0:
            grades_list.append('B+')
        elif g > 2.7:
            grades_list.append('B')
        elif g > 2.3:
            grades_list.append('B-')
        elif g > 2.0:
            grades_list.append('C+')
        elif g > 1.7:
            grades_list.append('C')
        elif g > 1.3:
            grades_list.append('C-')
        elif g > 1.0:
            grades_list.append('D+')
        elif g > 0.7:
            grades_list.append('D')
        elif g > 0.0:
            grades_list.append('D-')
        else:
            grades_list.append('E')
    return grades_list

print(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]))  # ['A+', 'B', 'C-', 'C', 'A-']

# In this function, we iterate over each grade in the input list, and based on the value of the grade, we add the corresponding letter grade to the grades_list.
# At the end, we return the grades_list which contains the letter grades corresponding to the input GPAs.
# This function assumes that the input list contains valid GPA values in the range [0.0, 4.0].
# If a grade outside this range is encountered, the function will return 'E' as the letter grade.
<jupyter_output>
['A+', 'B', 'C-', 'C', 'A-']
<jupyter_text>
Question 2: Write a Python function that takes a string containing a few words separated by spaces and returns a list of the words in reverse order.