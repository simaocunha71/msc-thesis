```
def max_Abs_Diff(arr):
    return max(arr) - min(arr)
```


The function `max_Abs_Diff` takes an array as input, finds the maximum and minimum values in the array using the built-in functions `max` and `min`, and then subtracts the minimum from the maximum to find the maximum difference between any two elements in the array. This is a simple and efficient solution. 

The unit test `assert max_Abs_Diff((2,1,5,3)) == 4` confirms that the function works correctly, as the maximum difference between the elements in the array `(2,1,5,3)` is indeed `4`. 

This solution assumes that the array contains at least two elements. If the array can be empty or contain only one element, additional checks would be needed to handle these edge cases. 

For example, the function could return `0` if the array is empty or `0` if the array contains only one element. Alternatively, it could raise an error in these cases if the function is not intended to handle them. 

Here is the updated function with these edge cases handled:

```
def max_Abs_Diff(arr):
    if len(arr) < 2:
        return 0
    return max(arr) - min(arr)
```


This updated function will return `0` if the array is empty or contains only one element, and will still return the maximum difference between any two elements in the array if it contains at least two elements.  It will also work correctly if the array contains non-numeric values, as it uses the built-in `max` and `min` functions, which can handle non-numeric values by treating them as if they were `float('inf')`.  However, if the array is expected to only contain numeric values, and the function is intended to work with non-numeric values, the function could be modified to handle this case.  For example, it could filter out non-numeric values before finding the maximum and minimum.  Here is an updated function that does this:

```
def max_Abs_Diff(arr):
    if len(arr) < 2:
        return 0
    nums = [x for x in arr if isinstance(x, (int, float))]
    if len(nums) < 2:
        return 0
    return max(nums) - min(nums)
```


This updated function will filter out any non-numeric values from the array before