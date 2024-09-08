
def square_nums(lst):
    return [i**2 for i in lst]

print(square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""
Output:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""

"""
Explanation:
The function square_nums takes in a list of numbers as input.
It returns a new list where each element is the square of the corresponding element in the input list.
The expression [i**2 for i in lst] is a list comprehension that does this.
"""
<jupyter_output>
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
<jupyter_text>
Problem 18:
<jupyter_code>
"""
