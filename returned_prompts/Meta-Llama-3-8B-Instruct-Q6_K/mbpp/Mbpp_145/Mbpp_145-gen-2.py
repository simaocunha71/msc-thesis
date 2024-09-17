```
def max_Abs_Diff(arr):
    return max(arr) - min(arr)
```


The problem is asking to find the maximum difference between any two elements in a given array. For example, in the array (2,1,5,3), the maximum difference is 5-1=4.

The unit test `assert max_Abs_Diff((2,1,5,3)) == 4` suggests that the function should return the maximum difference between any two elements in the array.

Here is a Python function that solves the problem:
```
def max_Abs_Diff(arr):
    return max(arr) - min(arr)
```
This function works by first finding the maximum and minimum values in the array using the built-in `max` and `min` functions. Then, it returns the difference between the maximum and minimum values, which is the maximum difference between any two elements in the array.