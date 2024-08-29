
def cube_nums(num_list):
    return [i ** 3 for i in num_list]

print(cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""
The function cube_nums takes a list of numbers as an argument and returns a new list with the cubes of the numbers from the input list.

The cube of a number is calculated by raising the number to the power of 3. The 'for' loop in the list comprehension iterates over each element i in the input list, and the expression i ** 3 calculates the cube of i.
"""

# Alternate Solution
def cube_nums(num_list):
    return [pow(i, 3) for i in num_list]

print(cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""
Both solutions use the same concept but the second one uses the built-in python function pow() which can be used to raise any number to a power.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
