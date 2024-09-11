def big_sum(arr):
    arr.sort()
    return arr[-1] + arr[0]


# Testing the function
assert big_sum([1,2,3]) == 4

"""
This function takes an array as an argument and first sorts the array in ascending order using the `sort()` method. Then, it returns the sum of the last element of the array (which is the largest value) and the first element of the array (which is the smallest value).

In the test case provided, the array `[1,2,3]` is passed to the function, which correctly sorts the array to `[1,2,3]`. The largest value is `3` and the smallest value is `1`, so the sum of these values is `4`. The function correctly returns `4`, as expected.
"""

```python
def big_sum(arr):
    arr.sort()
    return arr[-1] + arr[0]

# Testing the function
assert big_sum([1,2,3]) == 4
```

This Python function uses the `sort()` method to sort the array in ascending order, and then adds the last element (which is the largest value) and the first element (which is the smallest value) to get the desired sum. The `assert` statement is used to verify that the function correctly returns the expected result for the given test case.

The time complexity of this function is O(n log n) due to the sorting operation, and the space complexity is O(1) as it does not require any additional space.

Overall, this function provides an efficient solution to find the sum of the largest and smallest values in a given array.

```python
def big_sum(arr):
    arr.sort()
    return arr[-1] + arr[0]

# Testing the function
assert big_sum([1,2,3]) == 4
```

This function can be used in various scenarios where you need to find the sum of the largest and smallest values in an array. It can be easily integrated into existing Python codebases and provides a reliable solution to this problem.

To use this function in your own code, you can simply copy and paste the provided code into your Python script or