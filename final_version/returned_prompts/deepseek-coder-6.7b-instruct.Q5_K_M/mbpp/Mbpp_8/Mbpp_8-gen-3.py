def square_nums(nums):
    return [num ** 2 for num in nums]

print(square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""
The function square_nums takes a list of numbers as input. It uses a list comprehension to square each number in the list and returns a new list of the squared numbers.

The list comprehension works by iterating over each number in the input list (num for num in nums) and squaring it (num ** 2). The squared numbers are collected into a new list which is then returned by the function.
"""

# OR
def square_nums(nums):
    return list(map(lambda x: x ** 2, nums))

print(square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Both of these programs will return the same output.
<jupyter_output>
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
<jupyter_text>
Question 2:
<jupyter_code>
