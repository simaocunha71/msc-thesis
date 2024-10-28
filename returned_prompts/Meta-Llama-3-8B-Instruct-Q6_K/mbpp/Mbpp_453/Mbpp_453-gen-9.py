```
def sumofFactors(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 == 0:
            sum += i
    return sum
```
The function `sumofFactors(n)` iterates over all numbers from 1 to `n` (inclusive). For each number `i`, it checks if `i` is a factor of `n` (i.e., `n % i == 0`) and if `i` is even (i.e., `i % 2 == 0`). If both conditions are met, it adds `i` to the sum. Finally, it returns the sum of all even factors of `n`. 

For example, for `n = 18`, the even factors are `2`, `4`, `6`, `9`, `18`, and the sum is `2 + 4 + 6 + 18 = 26`. This function is tested by the unit test `assert sumofFactors(18) == 26`. 