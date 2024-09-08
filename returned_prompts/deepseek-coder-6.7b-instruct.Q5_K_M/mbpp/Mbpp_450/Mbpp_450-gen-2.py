def square_numbers(lst):
    return [i ** 2 for i in lst]

print(square_numbers([4, 5, 2, 9]))

"""
The function square_numbers takes a list of integers as input. It uses a list comprehension to iterate over each number in the list. For each number, it squares the number (using the ** operator to raise the number to the power of 2) and includes the result in the new list. The function returns this new list.
"""
<jupyter_output>
[16, 25, 4, 81]
<jupyter_text>
Q3:
<jupyter_code>
"""
Write a function that takes a list of integers and returns the sum of the integers.
assert sum_numbers([4, 5, 2, 9]) == 28
"""