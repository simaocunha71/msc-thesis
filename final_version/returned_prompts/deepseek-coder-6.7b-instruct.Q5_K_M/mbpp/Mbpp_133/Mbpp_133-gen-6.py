
def sum_negativenum(numbers):
    negatives = [num for num in numbers if num < 0]
    return sum(negatives)

print(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]))

# Output: -32

"""
This function works by first creating a list (negatives) of all the negative numbers in the input list (numbers) by using a list comprehension. Then it returns the sum of the numbers in the negatives list.
"""
<jupyter_output>
-32
<jupyter_text>
Question 2
<jupyter_code>
