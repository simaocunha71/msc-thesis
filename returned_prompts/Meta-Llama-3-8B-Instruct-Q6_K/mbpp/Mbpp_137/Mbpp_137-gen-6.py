```python
def zero_count(arr):
    zero = sum(1 for x in arr if x == 0)
    non_zero = len(arr) - zero
    return zero / non_zero if non_zero > 0 else 0
```



This function takes an array of integers as input and returns the ratio of zeroes to non-zeroes in the array. If there are no non-zero elements, it returns 0. The unit test `assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)` ensures that the function works correctly. The `math.isclose` function is used to compare the result with the expected value, allowing for a small tolerance due to floating-point arithmetic. The ratio is calculated by summing the number of zeroes and subtracting it from the total length of the array, then dividing by the number of non-zero elements. If there are no non-zero elements, the ratio is set to 0. The unit test ensures that the function returns the correct ratio.