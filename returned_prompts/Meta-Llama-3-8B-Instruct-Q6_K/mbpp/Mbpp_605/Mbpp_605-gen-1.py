```
def prime_num(n):
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


This function checks if a number is prime by first handling the special cases where the number is less than or equal to 1, or if it's 2, which is the only even prime number. Then it checks if the number is divisible by any number up to the square root of the number. If it is, then the number is not prime. If it's not divisible by any of these numbers, then it's prime. The function returns True if the number is prime, and False otherwise. The unit test `assert prime_num(13) == True` checks if the function correctly identifies the prime number 13. 





