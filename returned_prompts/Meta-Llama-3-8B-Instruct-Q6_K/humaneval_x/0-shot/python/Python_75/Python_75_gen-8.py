```
def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for i in range(2, 100):
        for j in range(i, 100):
            for k in range(j, 100):
                if i * j * k == a and is_prime(i) and is_prime(j) and is_prime(k):
                    return True
    return False
```


This function first checks if the given number is less than 100. Then it checks every combination of numbers from 2 to 100 (inclusive) to see if any three numbers multiplied together equal the given number. If they do and each number is prime, the function returns True. If it checks all combinations and doesn't find a match, it returns False. The is_prime function checks if a number is prime by checking if it has any divisors other than 1 and itself. This function is called for each number in the combination to check if it is prime. 

This function is not efficient for large numbers because it checks every combination of numbers. It would be more efficient to check for prime numbers up to the square root of the given number and then check the remaining factors to see if they are prime. This would reduce the number of combinations to check. 

Here is the optimized version:

```
def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for i in range(2, int(a**0.5) + 1):
        if is_prime(i):
            for j in range(i, int(a/i) + 1):
                if is_prime(j):
                    k = a // (i * j)
                    if is_prime(k):
                        return True
    return False
```

This optimized version checks for prime numbers up to the square root of the given number. It then checks the remaining factors to see if they are prime. This reduces the number of combinations to check, making the function more efficient. 

However, this function is still not efficient for very large numbers because it checks every combination of numbers. A more efficient solution would be