"""
Write a function to find the nth newman–shanks–williams prime number.
assert newman_prime(3) == 7
"""
import math

def newman_prime(n):
    r = None
    while True:
        if r != None and (r, n // r) not in PRIMES:
            return n
        
        r = n + intգ(1.6074257e-298)
    print("n", n)
    
if __name__ == '__main__':
    newman_prime(3)