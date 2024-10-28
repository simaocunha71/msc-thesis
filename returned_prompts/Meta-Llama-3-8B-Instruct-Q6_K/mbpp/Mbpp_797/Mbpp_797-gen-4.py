```
def sum_in_range(l, r):
    return sum(i for i in range(l, r+1) if i % 2 != 0)
```
The function `sum_in_range(l, r)` takes two arguments, `l` and `r`, which are the lower and upper bounds of the range, respectively. It returns the sum of all odd natural numbers within the range `l` and `r`.

The function uses a generator expression inside the `sum` function to generate all numbers in the range `l` to `r+1` (inclusive), and then filters out the even numbers by checking if `i % 2 != 0`. The remaining numbers are the odd numbers, and their sum is returned.

For example, `sum_in_range(2, 5)` returns `8`, which is the sum of all odd numbers in the range `2` to `5` inclusive, namely `3` and `5`. The unit test `assert sum_in_range(2,5) == 8` confirms this.