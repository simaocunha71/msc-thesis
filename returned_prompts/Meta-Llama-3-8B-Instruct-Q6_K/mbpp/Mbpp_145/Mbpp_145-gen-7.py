```
def max_Abs_Diff(arr):
    return max(arr) - min(arr)
```


This function takes an array as an argument and returns the maximum absolute difference between any two elements in the array. It does this by subtracting the minimum value from the maximum value in the array.

The unit test provided, `assert max_Abs_Diff((2,1,5,3)) == 4`, ensures that the function works correctly. It checks that the function returns 4 when given the input array `(2,1,5,3)`. This is because the maximum difference between any two elements in this array is 4 (5-1). 

The function works by using the built-in Python functions `max` and `min` to find the maximum and minimum values in the array, and then subtracting the minimum from the maximum to find the maximum absolute difference. This approach is efficient and easy to understand. 





