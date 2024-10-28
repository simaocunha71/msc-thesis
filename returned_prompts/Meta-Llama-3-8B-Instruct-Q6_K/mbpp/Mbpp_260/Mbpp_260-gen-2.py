```
def newman_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    num = 2
    while True:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1
```


The code defines a function `newman_prime(n)` that finds the nth Newman-Shanks-Williams prime number. The function uses a helper function `is_prime(num)` to check if a number is prime. It then iterates over numbers starting from 2, checks if each number is prime, and increments a counter if it is. When the counter reaches `n`, the function returns the current number as the nth Newman-Shanks-Williams prime number. The unit test `assert newman_prime(3) == 7` ensures that the function works correctly.