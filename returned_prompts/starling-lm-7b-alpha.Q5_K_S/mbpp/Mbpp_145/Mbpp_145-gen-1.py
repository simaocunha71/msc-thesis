"""
def max_Abs_Diff(nums):
    return max(nums) - min(nums)

assert max_Abs_Diff((2,1,5,3)) == 4
"""

The above python function can be used to find the maximum difference between any two elements in a given array. The function `max_Abs_Diff` takes a list of numbers as input and returns the maximum absolute difference between any two elements in the list. The `max` function is used to find the maximum value in the list, and the `min` function is used to find the minimum value in the list. The maximum absolute difference is then calculated by subtracting the minimum value from the maximum value. The `assert` statement is used to verify that the function is correctly calculating the maximum absolute difference.

Here are some additional notes about the function:

- The function `max_Abs_Diff` takes a single argument, which is the list of numbers.
- The function uses the `max` and `min` functions to find the maximum and minimum values in the list.
- The maximum absolute difference is calculated by subtracting the minimum value from the maximum value.
- The `assert` statement is used to verify that the function is correctly calculating the maximum absolute difference.

Overall, this function provides a straightforward way to find the maximum difference between any two elements in a given array.

Here are some additional resources for further reading on this topic:

- [Python max() Function](https://www.geeksforgeeks.org/python-max-function/)
- [Python min() Function](https://www.geeksforgeeks.org/python-min-function/)
- [Python assert Statement](https://www.geeksforgeeks.org/python-assert-statement/)

I hope this helps! Let me know if you have any more questions.

Best,
[Your Name]
"""

# Python3 Program to Find Maximum Absolute Difference

# Function to find maximum absolute difference
def max_Abs_Diff(nums):
    return max(nums) - min(nums)

# Driver code
nums = [2, 1, 5, 3]
print(max_Abs_Diff(nums))
```
