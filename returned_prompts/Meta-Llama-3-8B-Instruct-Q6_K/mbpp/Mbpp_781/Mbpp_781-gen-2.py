```
def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count % 2 == 0
```


This function counts the number of divisors for a given number and checks if the count is even. The unit test `assert count_divisors(10)` ensures that the function works correctly. The function iterates over all numbers from 1 to the given number, checks if the given number is divisible by each number, and increments the count if it is. Finally, it returns a boolean value indicating whether the count is even.  The unit test `assert count_divisors(10)` ensures that the function works correctly. The function should return `True` for `count_divisors(10)` because the count of divisors for 10 is 4 (1, 2, 5, 10), which is even.