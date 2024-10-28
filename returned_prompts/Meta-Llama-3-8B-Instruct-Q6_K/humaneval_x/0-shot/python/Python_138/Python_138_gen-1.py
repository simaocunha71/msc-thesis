```
def is_equal_to_sum_even(n):
    for a in range(2, n+1, 2):
        for b in range(2, n+1, 2):
            for c in range(2, n+1, 2):
                for d in range(2, n+1, 2):
                    if a + b + c + d == n:
                        return True
    return False
```


The problem is to write a function that checks whether a given number `n` can be expressed as the sum of exactly 4 positive even numbers. The function `is_equal_to_sum_even(n)` should return `True` if `n` can be expressed as such a sum, and `False` otherwise.

The function uses a nested loop approach to iterate over all possible combinations of 4 positive even numbers. For each combination, it checks whether the sum of the numbers is equal to `n`. If it finds such a combination, it returns `True`. If no such combination is found after checking all possible combinations, it returns `False`.

In the example, `is_equal_to_sum_even(4)` returns `False` because there is no combination of 4 positive even numbers that sums up to 4. Similarly, `is_equal_to_sum_even(6)` returns `False` because there is no combination of 4 positive even numbers that sums up to 6. However, `is_equal_to_sum_even(8)` returns `True` because the numbers 2, 2, 2, and 2 can be added together to sum up to 8.