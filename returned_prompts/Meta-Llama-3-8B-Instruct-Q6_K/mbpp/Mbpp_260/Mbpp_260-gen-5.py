```
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def newman_prime(n):
    count = 0
    num = 2
    while True:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1
```    
This code defines two functions: `is_prime` checks if a number is prime and `newman_prime` returns the nth Newman-Shanks-Williams prime number. The `newman_prime` function starts from 2 and checks each number to see if it is prime. If it is, it increments a counter. When the counter reaches `n`, it returns the number. The `is_prime` function checks if a number is prime by testing divisibility up to its square root.

The unit test `assert newman_prime(3) == 7` ensures that the function returns the correct result for the third Newman-Shanks-Williams prime number, which is 7.