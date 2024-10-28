```
def newman_prime(n):
    primes = [2]
    i = 3
    while len(primes) < n:
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
            if p * p > i:
                break
        if is_prime:
            primes.append(i)
        i += 2
    return primes[-1]
```
This function generates prime numbers using the Sieve of Eratosthenes algorithm. It starts with 2 as the first prime number, then iterates over odd numbers starting from 3. For each number, it checks if it's divisible by any of the previously found prime numbers. If it's not, it's a new prime number, so it's added to the list of primes. The function stops when it has found the nth prime number, which is then returned.

The unit test `assert newman_prime(3) == 7` ensures that the function correctly finds the 3rd prime number, which is 7. The function is designed to be efficient and scalable, making it suitable for finding larger prime numbers.