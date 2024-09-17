```
import math
def zero_count(lst):
    zeroes = sum(1 for x in lst if x == 0)
    non_zeroes = len(lst) - zeroes
    return zeroes / non_zeroes if non_zeroes > 0 else 0
```


The provided unit test suggests that the ratio should be calculated as the number of zeroes divided by the number of non-zero elements in the array. This is a more accurate representation of the proportion of zeroes in the array.

Here is the Python function that implements this:

```
import math
def zero_count(lst):
    zeroes = sum(1 for x in lst if x == 0)
    non_zeroes = len(lst) - zeroes
    return zeroes / non_zeroes if non_zeroes > 0 else 0
```

This function works by counting the number of zeroes and non-zero elements in the array, and then returning the ratio of zeroes to non-zeroes. The `math.isclose` function is used to compare the result with the expected value, with a relative tolerance of 0.001. This means that the result is considered correct if it is within 0.1% of the expected value.