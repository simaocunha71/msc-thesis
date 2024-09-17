The problem is asking to write a function that takes an array as input and returns the sum of the largest and smallest values in the array.
However, the problem statement is not clear about whether we need to consider the sum of the absolute values of the largest and smallest values or not. 

Thanks to the unit test `assert big_sum([1,2,3]) == 4`, we can interpret the problem as finding the sum of the largest and smallest values in the array without considering their signs. This means that if the array contains both positive and negative numbers, the function will return the sum of the largest and smallest absolute values.

Here is the Python function that solves the problem:
```
def big_sum(arr):
    return max(arr) + min(arr)
```
This function uses the built-in `max` and `min` functions in Python to find the largest and smallest values in the array, and then returns their sum. The function does not consider the signs of the values, so it will work correctly even if the array contains both positive and negative numbers. 