```
import math

def zero_count(lst):
    zeros = sum(1 for x in lst if x == 0)
    non_zeros = len(lst) - zeros
    return zeros / non_zeros if non_zeros > 0 else 0
```
This function counts the number of zeroes and non-zero elements in the list, then returns the ratio of zeroes to non-zero elements. If there are no non-zero elements, it returns 0 to avoid division by zero.

The unit test `assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)` checks that the function returns the correct ratio for a given list. The `math.isclose` function is used to compare the result to the expected value with a relative tolerance of 0.001. This allows for small differences due to floating point precision. 