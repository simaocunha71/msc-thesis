```
def zero_count(arr):
    zero = 0
    non_zero = 0
    for num in arr:
        if num == 0:
            zero += 1
        else:
            non_zero += 1
    return zero / (zero + non_zero) if zero + non_zero > 0 else 0
```
The function `zero_count` takes an array of integers as an argument. It iterates over the array, counting the number of zeroes and non-zeroes. The ratio is then calculated by dividing the count of zeroes by the total count of zeroes and non-zeroes. If the total count is zero, the function returns 0 to avoid division by zero.

The unit test `assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)` ensures that the function correctly calculates the ratio of zeroes to non-zeroes. The `math.isclose` function is used to compare the result with the expected value, allowing for a small tolerance due to floating point precision issues.