"""
This problem can be solved by using a simple prime generating function and storing the generated primes in a list. The function newman_prime(n) will return the nth prime number in the list.
"""

def generate_prime(limit):
    primes = [2]
    num = 3
    while len(primes) < limit:
        if all(num % prime != 0 for prime in primes):
            primes.append(num)
        num += 2
    return primes

def newman_prime(n):
    primes = generate_prime(10000)
    return primes[n-1]

assert newman_prime(3) == 7
"""

