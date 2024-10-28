```
def _sum(arr):
    return sum(arr)
```


The problem asks to write a function that calculates the sum of an array. The function should take an array as input and return the sum of its elements. 

The unit test `assert _sum([1, 2, 3]) == 6` indicates that the function should return the sum of the array elements. 

The solution uses Python's built-in `sum` function, which calculates the sum of all elements in an iterable (like a list). So, we can simply use `sum(arr)` to return the sum of the array elements. 

Here is the solution:
```
def _sum(arr):
    return sum(arr)
```


This function works by passing the input array `arr` to the `sum` function, which returns the sum of all elements in the array. The result is then returned by the `_sum` function. 

This solution is efficient and easy to understand, and it passes the given unit test. 

For example, if we call `_sum([1, 2, 3])`, it will return `6`, which is the sum of the elements in the array. 

Note: The `sum` function is a built-in function in Python, so we don't need to define it ourselves. We can simply use it to calculate the sum of an array. 