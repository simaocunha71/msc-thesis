
def filter_oddnumbers(numbers):
    return [num for num in numbers if num % 2 == 0]

print(filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""
Here, I've used a list comprehension to iterate over each number in the input list. If the remainder of the number divided by 2 is zero (i.e., the number is even), it's included in the new list. If not, it's skipped.
"""
<jupyter_output>
[2, 4, 6, 8, 10]
<jupyter_text>
Problem 2
<jupyter_code>
