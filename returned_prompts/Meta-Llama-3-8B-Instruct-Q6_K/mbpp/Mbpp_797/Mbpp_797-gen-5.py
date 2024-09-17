```
def sum_in_range(l, r):
    return sum(range(l, r + 1, 2))
```


The function `sum_in_range` takes two parameters `l` and `r` representing the lower and upper bounds of the range. It uses the built-in `range` function to generate a sequence of numbers from `l` to `r` (inclusive) with a step size of 2, which means it will generate all odd numbers in the range. The `sum` function is then used to calculate the sum of these odd numbers.

The unit test `assert sum_in_range(2,5) == 8` ensures that the function works correctly by checking that the sum of all odd numbers between 2 and 5 (inclusive) is indeed 8. This test helps to verify that the function is working as expected.