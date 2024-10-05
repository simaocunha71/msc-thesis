```
def is_equal_to_sum_even(n):
    for a in range(2, n+1, 2):
        for b in range(a+2, n+1, 2):
            for c in range(b+2, n+1, 2):
                for d in range(c+2, n+1, 2):
                    if a + b + c + d == n:
                        return True
    return False
```


Note: The function `is_equal_to_sum_even(n)` checks whether the given number `n` can be written as the sum of exactly 4 positive even numbers. It does this by iterating over all possible combinations of even numbers and checking if the sum of these numbers equals `n`. If it finds such a combination, it returns `True`; otherwise, it returns `False`. The time complexity of this function is O(n), which is not very efficient for large values of `n`. A more efficient solution would be to use dynamic programming, but it would also be more complex. For small values of `n`, this function should work fine.