The task is to write a Python function that finds the sum of an array. 

The provided unit test `assert _sum([1, 2, 3]) == 6` suggests that the function should take an array as input and return the sum of its elements.

Here's a simple solution using the built-in `sum` function:
```
def _sum(arr):
    return sum(arr)
```
This function works by passing the input array `arr` to the `sum` function, which returns the sum of all elements in the array. The result is then returned by the `_sum` function. 

For example, if you call `_sum([1, 2, 3])`, it will return `6`, which is the sum of the elements in the array. 

Note: This solution assumes that the input array only contains numbers. If the array can contain non-numeric elements, you may need to add error handling or modify the function to handle those cases. 