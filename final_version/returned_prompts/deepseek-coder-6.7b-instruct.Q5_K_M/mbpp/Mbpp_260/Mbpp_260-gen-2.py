"""
The function newman_prime(n) will find the nth newman–shanks–williams prime number.

Input:
- n: integer

Output:
- prime: integer

Steps:
1. Initialize a list of known newman–shanks–williams primes: [2, 3, 5, 7, 11]
2. If n is less than or equal to 5, return the nth element of the list.
3. Else, find the next newman–shanks–williams prime by:
    a. Initialize the next_prime variable as the last element in the list.
    b. Increment the next_prime until it is a newman–shanks–williams prime.
    c. Append the new newman–shanks–williams prime to the list.
4. Return the nth newman–shanks–williams prime.
"""

def newman_prime(n):
    newman_primes = [2, 3, 5, 7, 11]
    if n <= 5:
        return newman_primes[n-1]
    else:
        next_prime = newman_primes[-1] + 1
        while True:
            if is_newman_prime(next_prime):
                newman_primes.append(next_prime)
                if len(newman_primes) == n:
                    return newman_primes[-1]
            next_prime += 1

def is_newman_prime(num):
    if num in [2, 3, 5, 7, 11]:
        return True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Testing the function
assert newman_prime(3) == 7
assert newman_prime(4) == 13
assert newman_prime(5) == 19
assert newman_prime(6) == 31
assert newman_prime(7) == 43
assert newman_prime(8) == 67
assert newman_prime(9)