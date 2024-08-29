"""
The Newman–Shanks–Williams prime are the prime numbers that are congruent to 2, 3, 4, 6, 7 modulo 8. 

To find the nth Newman–Shanks–Williams prime, we can use a while loop to continuously find prime numbers and store them in a list. We will continue until we find n amount of primes. 

We will use the sympy library to generate prime numbers.

We will start by defining the function newman_prime which takes in an integer n.
"""

import sympy

def newman_prime(n: int) -> int:
    if n <= 0:
        raise ValueError("n must be a positive integer")

    primes = []
    num = 2
    while len(primes) < n:
        if sympy.isprime(num):
            primes.append(num)
        num += 1

    return primes[-1]

assert newman_prime(3) == 7
"""
The function newman_prime starts by checking if n is less than or equal to 0 and raises a ValueError if so.

Then, it initializes an empty list primes and a variable num set to 2.

The while loop continues until we have found n amount of primes. Inside the loop, we use sympy.isprime() to check if num is prime, and if so, we append it to primes. After that, we increment num by 1.

Finally, the function returns the last element in the primes list, which is the nth Newman–Shanks–Williams prime.
"""

"""
This function works by continuously checking each number if it is a prime number. It stores all the prime numbers found in a list until it has found n prime numbers. The last prime number in the list is then returned.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
