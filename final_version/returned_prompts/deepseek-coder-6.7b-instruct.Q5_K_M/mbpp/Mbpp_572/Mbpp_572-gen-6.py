"""
We will use Python's built-in 'sum' function to calculate the sum of the numbers and then divide it by the number of elements to get the mean.
"""

def mean(nums):
    return sum(nums) / len(nums)

print(mean([1,2,3,4,5]))


"""
The function 'mean' takes a list 'nums' as input. It returns the result of the sum of the numbers divided by the length of the list.

When we run the code with the input [1,2,3,4,5], the output is 3.0 which is correct.
"""
<jupyter_output>
3.0
<jupyter_text>
Q3:
<jupyter_code>
"""
Write a python function that takes a list of numbers and returns a dictionary with the minimum and maximum numbers as keys and their corresponding values as the count of these numbers in the list.
assert min_max