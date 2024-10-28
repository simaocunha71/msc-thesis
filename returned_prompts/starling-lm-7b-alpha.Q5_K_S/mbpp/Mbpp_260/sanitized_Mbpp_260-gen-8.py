from math import gcd
from typing import List, Optional, Tuple
def newman_prime(n: int) -> int:
    if n < 2:
        raise ValueError("newman_prime requires an integer n >= 2")
    # Initialize constants and variables
    a, b, c = 1, 1, 1
    m1, m2 = 1, 1
    r1, r2 = 1, 1
    s1, s2 = 1, 1
    # Iterate n times
    for _ in range(n):
        # Update m1, m2, r1, r2, s1, s2
        m1, m2, r1, r2, s1, s2 = m2, m1, r2, r1, s2, s1
        # Update a, b, c
        a, b, c = (
            (a + b) % m1,
            (b + c) % m1,
            (c + a) % m1,
        )
        # Update r1, r2, s1, s2
        r1, r2, s1, s2 = (
            (r1 + r2) % m2,
            (r2 + s1) % m2,
            (s1 + r1) % m2,
            (s2 + s1) % m2,
        )
        # Check if r2 is prime
        if r2 == 1:
            continue
        # Check if r2 is prime and gcd(r2 - 1, m1) = 1
        if gcd(r2 - 1, m1) == 1:
            return r2
    # If we reach here, we exceeded the nth newman–shanks–williams prime number
    raise ValueError("newman_prime exceeded the nth newman–shanks–williams prime number")