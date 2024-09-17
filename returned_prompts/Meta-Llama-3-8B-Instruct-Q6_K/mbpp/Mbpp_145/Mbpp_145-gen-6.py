You can use the built-in `max` function to find the maximum and minimum values in the array, and then subtract the minimum from the maximum to find the maximum difference.

Here is the Python function:

```
def max_Abs_Diff(arr):
    return max(arr) - min(arr)
```

This function works by finding the maximum value in the array using the `max` function, and the minimum value using the `min` function. It then subtracts the minimum from the maximum to find the maximum difference.

For example, if you call `max_Abs_Diff((2,1,5,3))`, the function will return `4`, which is the maximum difference between any two elements in the array. The maximum difference is between the element `5` and the element `1`, which is `4`.