```
import math

def sum_squares(lst):
    return round(sum(math.ceil(i) ** 2 for i in lst))
```


Explanation:
This function uses a generator expression to calculate the sum of the squares of the elements in the list, after rounding each element up to the nearest integer using the `math.ceil` function. The `sum` function is then used to add up these squared values. The result is rounded to the nearest integer using the `round` function.