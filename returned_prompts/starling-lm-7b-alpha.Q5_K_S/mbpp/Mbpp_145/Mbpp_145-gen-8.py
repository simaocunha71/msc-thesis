Here is a Python function that uses the built-in `max` function to find the maximum difference between any two elements in a given array:

```python
def max_Abs_Diff(arr):
    return max(abs(i - j) for i, j in zip(arr, arr[1:]))
```

Here's an explanation of the `max_Abs_Diff` function:

1. The function `max_Abs_Diff` takes an array (`arr`) as input.
2. The expression `abs(i - j) for i, j in zip(arr, arr[1:])` calculates the absolute difference between each pair of adjacent elements in the array. The `zip` function is used to iterate through the array and its subsequent elements.
3. The `max` function is used to find the maximum value among the calculated absolute differences.
4. The result is returned by the function.

To test the function, you can use the provided `assert` statement:

```python
assert max_Abs_Diff((2,1,5,3)) == 4
```

This assertion checks if the `max_Abs_Diff` function correctly calculates the maximum absolute difference in the given array `(2, 1, 5, 3)`, which should be equal to `4`. If the assertion passes, no error message will be displayed.

It's important to note that the `max_Abs_Diff` function assumes that the input array is non-empty and consists of numeric values. If you want to handle edge cases such as empty arrays or non-numeric values, you can add additional error checking in the function.

Additionally, if you need to find the maximum absolute difference between any two elements in an array of more than two dimensions, you can use the `numpy` library's `ndarray.ptp` function. Here's an example of how to use it:

```python
import numpy as np

def max_Abs_Diff(arr):
    return np.ptp(arr)
```

The `np.ptp` function calculates the difference between the maximum and minimum values of an array, which is equivalent to finding the maximum absolute difference.

You can also use the `numpy` library's