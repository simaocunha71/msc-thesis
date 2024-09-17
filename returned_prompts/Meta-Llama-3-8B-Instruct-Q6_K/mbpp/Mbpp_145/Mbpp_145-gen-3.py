```
def max_Abs_Diff(arr):
    return max(arr) - min(arr)
```
This function calculates the maximum difference between any two elements in the given array by subtracting the minimum value from the maximum value in the array. The unit test `assert max_Abs_Diff((2,1,5,3)) == 4` ensures that the function works correctly for the given input. The function assumes that the input array is not empty. If the input array is empty, it will raise an exception when trying to calculate the minimum and maximum values. To handle this, you can add a check at the beginning of the function to return a specific value or raise an exception if the array is empty. For example:
```
def max_Abs_Diff(arr):
    if not arr:
        return 0  # or raise ValueError("Array is empty")
    return max(arr) - min(arr)
```



