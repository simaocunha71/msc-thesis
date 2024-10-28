```
def divisor(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count
```



The function `divisor(n)` takes an integer `n` as input and returns the number of divisors it has. It does this by iterating over all numbers from 1 to `n` and checking if `n` is divisible by each number. If it is, it increments a counter. Finally, it returns the counter, which represents the number of divisors of `n`.

This solution passes the unit test `assert divisor(15) == 4`, which checks that the number of divisors of 15 is 4 (1, 3, 5, and 15).