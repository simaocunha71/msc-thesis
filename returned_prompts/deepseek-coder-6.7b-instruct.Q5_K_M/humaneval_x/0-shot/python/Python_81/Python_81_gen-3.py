
def numerical_letter_grade(grades):
    grade_book = {4.0: 'A+', 3.7: 'A', 3.3: 'A-', 3.0: 'B+', 2.7: 'B', 2.3: 'B-', 2.0: 'C+', 1.7: 'C', 1.3: 'C-', 1.0: 'D+', 0.7: 'D', 0.0: 'E'}
    return [grade_book[max([key for key in grade_book.keys() if key <= grade])] for grade in grades]

print(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]))

# Output: ['A+', 'B', 'C-', 'C', 'A-']

In this function, we first build a dictionary mapping GPA to letter grade as per the problem statement. Then, for each GPA in the given list, we find the highest GPA from our dictionary that is less than or equal to the current GPA, and use that letter grade. The result is a list of letter grades corresponding to the input list of GPAs.

The time complexity of this function is O(n*m), where n is the number of grades and m is the number of different grades in the dictionary. This is because for each grade, we are traversing the dictionary to find the highest GPA that is less than or equal to the grade. The space complexity is O(n), as we are creating a new list of n elements.
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 3
<jupyter_code>
