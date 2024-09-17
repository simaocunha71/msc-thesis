```
def max_Abs_Diff(arr):
    return max(arr) - min(arr)
```
This function works by finding the maximum and minimum values in the array and then subtracting the minimum from the maximum. This will give the maximum difference between any two elements in the array.

The unit test `assert max_Abs_Diff((2,1,5,3)) == 4` ensures that the function works correctly. It checks that the maximum difference between the elements in the array `(2,1,5,3)` is `4` (which is the difference between `5` and `1`).

This function assumes that the input is a non-empty array of numbers. If the input can be empty or contain non-numeric values, additional error checking would be needed. 

For example, if the input can be empty, you could add a check at the beginning of the function to raise an error if the input is empty. If the input can contain non-numeric values, you could add a check to raise an error if any element in the array is not a number. 

Here is an example of how you could add these checks:
```
def max_Abs_Diff(arr):
    if len(arr) == 0:
        raise ValueError("Input array is empty")
    for x in arr:
        if not isinstance(x, (int, float)):
            raise ValueError("Input array contains non-numeric values")
    return max(arr) - min(arr)
``` 












