```
def newman_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes[-1]
```
The problem asks to write a function that finds the nth Newman-Shanks-Williams prime number. The function should use a helper function to check if a number is prime.

The provided unit test `assert newman_prime(3) == 7` suggests that the function should return the 3rd Newman-Shanks-Williams prime number, which is 7.

Here is the solution. The function `newman_prime(n)` uses a helper function `is_prime(num)` to check if a number is prime. It starts from 2 and checks each number until it finds the nth prime number. The function returns the nth prime number.

The helper function `is_prime(num)` checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of the numbers in that range. If the number is not divisible, it is prime. If it is divisible, it is not prime.

The main function `newman_prime(n)` uses a list `primes` to store the prime numbers found. It starts from 2 and checks each number until it finds the nth prime number. The function returns the nth prime number.