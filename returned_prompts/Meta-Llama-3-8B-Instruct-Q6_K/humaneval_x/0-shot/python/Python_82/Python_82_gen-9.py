```
def prime_length(string):
    length = len(string)
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    return is_prime(length)
```


The function `prime_length(string)` calculates the length of the input string and checks if it's a prime number. It uses a helper function `is_prime(n)` to determine if a number is prime. This helper function checks if the number is divisible by any number from 2 up to its square root. If it is, then the number is not prime and the function returns `False`. If the number is not divisible by any of these, it's prime and the function returns `True`. The `prime_length(string)` function then returns the result of `is_prime(length)`, where `length` is the length of the input string.