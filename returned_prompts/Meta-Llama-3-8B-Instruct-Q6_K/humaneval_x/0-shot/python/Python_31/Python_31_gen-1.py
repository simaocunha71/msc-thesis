```
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True
```
This function checks if a given number `n` is prime or not. It first checks if `n` is less than or equal to 1 (in which case it's not prime), or if `n` is 2 (which is prime). If `n` is even, it's not prime. Then it checks divisibility up to the square root of `n`, and if `n` is divisible by any of these numbers, it's not prime. If `n` passes all these checks, it's prime. 

The time complexity of this function is O(sqrt(n)), as it needs to check up to the square root of `n` for divisibility. The space complexity is O(1), as it only uses a constant amount of space. 





