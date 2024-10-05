```
def count_up_to(n):
    if n < 1:
        return []
    
    primes = []
    num = 2
    while num < n:
        if is_prime(num):
            primes.append(num)
        num += 1

    return primes


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
```
This code defines two functions: `count_up_to` and `is_prime`. 

The `count_up_to` function takes an integer `n` as input and returns an array of the first `n` integers that are prime numbers and less than `n`. It starts a counter `num` from 2 and checks if each number is prime using the `is_prime` function. If the number is prime, it adds it to the `primes` list. It stops the loop when `num` is greater than or equal to `n`. Finally, it returns the `primes` list.

The `is_prime` function takes an integer `num` as input and returns `True` if it is a prime number, and `False` otherwise. It checks if `num` is less than 2, in which case it is not prime. Then it checks if `num` is divisible by any number from 2 to the square root of `num`. If it is divisible, it is not prime. Otherwise, it is prime. 

You can test the `count_up_to` function with different inputs to see the expected output. For example, `count_up_to(5)` should return `[2, 3]`. 

Note that the `is_prime` function is not the most efficient way to check for primality, especially for large numbers. There are more efficient algorithms available, such as the Miller-Rabin primality test. However, this simple trial division method is sufficient for small inputs. 














