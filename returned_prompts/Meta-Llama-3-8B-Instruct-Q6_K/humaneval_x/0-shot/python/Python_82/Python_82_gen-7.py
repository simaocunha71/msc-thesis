```
def prime_length(string):
    length = len(string)
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    return is_prime(length)
```


This function first calculates the length of the input string. It then defines a helper function `is_prime` to check if a number is prime. The `is_prime` function checks divisibility from 2 to the square root of the number, and returns `True` if the number is prime, and `False` otherwise. Finally, the function returns the result of applying `is_prime` to the length of the input string.