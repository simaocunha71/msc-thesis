```
def max_Abs_Diff(arr):
    return max(arr) - min(arr)
```


Explanation:
The problem is asking for a function that finds the maximum difference between any two elements in a given array. 

The unit test provided, `assert max_Abs_Diff((2,1,5,3)) == 4`, suggests that the function should return the absolute difference between the maximum and minimum values in the array.

This can be achieved by using the built-in `max` and `min` functions in Python, which return the maximum and minimum values in the array, respectively. The absolute difference between these two values is calculated using the `-` operator and the `abs` function.

Here is the Python function that solves the problem:
```
def max_Abs_Diff(arr):
    return max(arr) - min(arr)
```


This function takes an array as input, calculates the maximum and minimum values in the array, and returns their absolute difference. The `max` function returns the maximum value in the array, the `min` function returns the minimum value, and the `-` operator subtracts the minimum value from the maximum value. The result is the maximum difference between any two elements in the array.