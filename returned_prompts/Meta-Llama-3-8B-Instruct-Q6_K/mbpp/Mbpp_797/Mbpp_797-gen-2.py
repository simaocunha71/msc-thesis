```
def sum_in_range(l, r):
    return sum(i for i in range(l, r+1) if i % 2 != 0)
```


The function `sum_in_range` takes two arguments `l` and `r` which are the lower and upper bounds of the range. It uses a generator expression to iterate over the range and sum up all the odd numbers in the range. The condition `i % 2 != 0` checks if a number is odd. The `sum` function is used to add up all the odd numbers in the range.

The unit test `assert sum_in_range(2,5) == 8` ensures that the function works correctly. The sum of all odd natural numbers within the range 2 and 5 is indeed 8 (3 + 5).