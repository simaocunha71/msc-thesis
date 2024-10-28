```
import math

def zero_count(lst):
    zeroes = sum(1 for x in lst if x == 0)
    non_zeroes = len(lst) - zeroes
    if non_zeroes == 0:
        return 0
    return zeroes / non_zeroes
```


The problem asks to write a function that calculates the ratio of zeroes to non-zeroes in an array of integers. The function should take an array as input and return this ratio.

The unit test `assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)` helps to understand the problem better. It tests the function with an array and checks if the returned ratio is close to 0.181818.

The solution uses a generator expression to count the number of zeroes in the array, and then calculates the ratio by dividing the number of zeroes by the number of non-zeroes. If there are no non-zeroes, the function returns 0. The `math.isclose` function is used to compare the returned ratio with the expected value, with a relative tolerance of 0.001. This means that the function will consider the returned ratio close to 0.181818 if it is within 0.001 of this value.