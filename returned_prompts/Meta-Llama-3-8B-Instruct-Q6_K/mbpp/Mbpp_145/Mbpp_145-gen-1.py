The problem is asking to find the maximum difference between any two elements in a given array. 

Here is the python function that solves this problem:

```Python
def max_Abs_Diff(arr):
    return max(arr) - min(arr)
```

This function works by subtracting the smallest element (found with `min(arr)`) from the largest element (found with `max(arr)`) in the array. 

For example, if the input array is `(2,1,5,3)`, the function will return `4` which is the maximum difference between any two elements in the array. 

The unit test `assert max_Abs_Diff((2,1,5,3)) == 4` also confirms that this function works correctly. 





The function works by simply subtracting the smallest element from the largest element in the array. This is because the maximum difference between any two elements will always be between the largest and smallest elements in the array. The `max` function returns the largest element in the array, and the `min` function returns the smallest element in the array. The difference between these two elements is the maximum difference between any two elements in the array.