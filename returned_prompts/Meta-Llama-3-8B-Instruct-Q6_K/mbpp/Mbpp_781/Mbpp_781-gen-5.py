```
def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count % 2 == 0

print(count_divisors(10))  # True
```


This function counts the number of divisors of a given number `n`. It iterates over all numbers from 1 to `n` and checks if `n` is divisible by each number. If it is, it increments the count. Finally, it returns whether the count is even (i.e., `count % 2 == 0`). The unit test `assert count_divisors(10)` checks if the function correctly returns `True` for the number 10, which has an even number of divisors (1, 2 and 5, 10). 

Note: The unit test `assert count_divisors(10)` is used to check the function's output. The function `count_divisors` is expected to return `True` for the input `10`. The unit test ensures that the function returns the expected output. If the function returns anything other than `True`, the unit test will fail, indicating that the function is not working correctly. This helps in debugging and ensuring the correctness of the function. 














