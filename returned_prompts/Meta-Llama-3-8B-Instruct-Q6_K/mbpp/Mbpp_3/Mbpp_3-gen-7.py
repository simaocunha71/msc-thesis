```
def is_not_prime(n):
    if n <= 1:
        return True
    elif n <= 3:
        return False
    elif n % 2 == 0 or n % 3 == 0:
        return True
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return True
        i += 6
    return False
```
The function is_not_prime checks if a number is not prime. It first checks if the number is less than or equal to 1 (in which case it is not prime), or if the number is less than or equal to 3 (in which case it is prime). Then it checks if the number is divisible by 2 or 3. If it is, then it is not prime. If none of these conditions are met, then it checks divisibility up to the square root of the number, incrementing the divisor by 6 each time (since all primes are of the form 6k ± 1). If the number is divisible by any of these divisors, then it is not prime. If it is not divisible by any of these divisors, then it is prime. The function returns True if the number is not prime, and False if it is. 

The unit test `assert is_not_prime(2) == False` ensures that the function correctly identifies prime numbers as False. The function can be used to identify non-prime numbers by calling it with the number as an argument, and checking if the returned value is True. 