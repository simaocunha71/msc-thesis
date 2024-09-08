def big_sum(arr):
    return max(arr) + min(arr)

print(big_sum([1,2,3])) # 4

"""
Explanation: 
The function big_sum takes an array as an argument. It uses the built-in Python functions max and min to find the largest and smallest values in the array, respectively. It then returns the sum of these two values.
"""

"""
This code works by:
1. Using the built-in Python functions `max()` and `min()` to find the maximum and minimum values in the list.
2. Adding these two values together and returning the result.
"""
<jupyter_output>
4
<jupyter_text>
2. Write a Python function that accepts a list of numbers and returns a new list with those numbers multiplied by 2 and then subtracted by 1.
<jupyter_code>
