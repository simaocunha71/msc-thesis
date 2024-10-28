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



The function `is_equal_to_sum_even(n)` checks if the given number `n` can be written as the sum of exactly 4 positive even numbers. It does this by iterating over all combinations of 4 even numbers (from 2 to `n` inclusive) and checking if their sum equals `n`. If a combination is found where the sum equals `n`, the function returns `True`. If no such combination is found after checking all combinations, the function returns `False`. The example test cases provided in the problem statement demonstrate the expected behavior of the function. For instance, `is_equal_to_sum_even(4)` returns `False` because there is no combination of 4 positive even numbers that sums to 4. On the other hand, `is_equal_to_sum_even(8)` returns `True` because the numbers 2, 2, 2, and 2 sum to 8.