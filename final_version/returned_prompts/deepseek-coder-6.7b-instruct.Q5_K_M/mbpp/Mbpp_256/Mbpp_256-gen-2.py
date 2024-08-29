def count_Primes_nums(n):
    if n < 2:
        return 0
    sieve = [1] * n
    sieve[0] = sieve[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n, i):
                sieve[j] = 0
    return sum(sieve)

# Test the function
print(count_Primes_primes(5)) # should return 2

# Explanation: The prime numbers less than 5 are 2 and 3.

"""
The function `count_Primes_nums` works by using the Sieve of Eratosthenes algorithm to generate a list of boolean values indicating whether each index is a prime number. The Sieve of Eratosthenes is an efficient algorithm used to find all primes smaller than a given number `n`. It does so by iteratively marking the multiples of each number starting from 2. 

In this case, we start from the number 2, and mark all its multiples. Then we move to the next unmarked number and repeat the process. We continue this until we have processed all numbers less than `n`. 

Finally, we sum up all the elements in the list to get the count of prime numbers.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 3:Write a Python function named "fact" that takes an integer n as an argument and returns the factorial of that number. The factorial of a number is the product of all positive integers less than or equal to n. If n is 0, the factorial is defined to be 1.
<jupyter_code>
# Solution
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

# Test the function
print(fact(5)) # should return 120

# Explanation: The factorial of 5 is 5*4*3*2*1 = 120
<jupyter_