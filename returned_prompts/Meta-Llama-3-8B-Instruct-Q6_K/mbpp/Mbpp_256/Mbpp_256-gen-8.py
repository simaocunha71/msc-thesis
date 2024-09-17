```
def count_Primes_nums(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    for i in range(2, n):
        if is_prime(i):
            count += 1
    return count
```
The function `count_Primes_nums` takes an integer `n` as an argument and returns the number of prime numbers less than `n`.

The helper function `is_prime` checks if a number is prime. It returns `False` for numbers less than 2, and then checks if the number is divisible by any number from 2 to the square root of the number. If it is divisible, it is not a prime number and the function returns `False`. If it is not divisible by any of these numbers, it is a prime number and the function returns `True`.

In the `count_Primes_nums` function, we iterate over all numbers from 2 to `n-1` and check if each number is prime using the `is_prime` function. If it is prime, we increment the count. Finally, we return the count. 

This solution passes the given unit test `assert count_Primes_nums(5) == 2`.  For example, `count_Primes_nums(5)` returns `2` because there are two prime numbers less than `5`: `2` and `3`.  Similarly, `count_Primes_nums(10)` returns `4` because there are four prime numbers less than `10`: `2`, `3`, `5`, and `7`.  This solution works correctly for all non-negative integers.  It has a time complexity of O(n*sqrt(n)) because it checks each number up to `n` to see if it is prime, and it checks up to the square root of each number to see if it is divisible by any other number.  This is not the most efficient solution, but it is simple and easy to understand.  For larger inputs, a more efficient solution would be needed.  For example, the Sieve of Eratosthenes algorithm is a more efficient way to find all prime numbers up to a certain number.  This algorithm works by iteratively marking as composite (not prime) the multiples of each prime number as it is encountered