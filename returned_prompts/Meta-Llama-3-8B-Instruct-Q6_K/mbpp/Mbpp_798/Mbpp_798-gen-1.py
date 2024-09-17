```
def _sum(arr):
    return sum(arr)
```


This function uses the built-in `sum` function in Python which adds up all the elements in the given array. 

The unit test `assert _sum([1, 2, 3]) == 6` ensures that the function correctly calculates the sum of the array. 

Please note that this function does not handle edge cases like an empty array or an array with non-numeric values. For a more robust solution, you might want to add error checking and handling for these cases. 

For example, you could add a check to return 0 if the array is empty, or raise an error if the array contains non-numeric values. 

Here is an example of how you could do this:
```
def _sum(arr):
    if not arr:
        return 0
    for i in arr:
        if not isinstance(i, (int, float)):
            raise ValueError("Array must only contain numbers")
    return sum(arr)
```


This version of the function will return 0 for an empty array, raise an error if the array contains non-numeric values, and correctly calculate the sum of the array if it contains only numbers. 