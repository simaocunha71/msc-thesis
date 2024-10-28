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


In this problem, we need to write a function that takes a non-negative integer as input and returns the number of prime numbers less than the given number.

The provided unit test `assert count_Primes_nums(5) == 2` helps us understand that the function should return the number of prime numbers less than the given number. For example, for the input 5, the function should return 2 because there are two prime numbers less than 5, which are 2 and 3.

The solution uses a helper function `is_prime` to check if a number is prime. The main function `count_Primes_nums` iterates over the range from 2 to the given number, checks each number to see if it's prime using the `is_prime` function, and increments a counter whenever it finds a prime number. Finally, it returns the count of prime numbers found.