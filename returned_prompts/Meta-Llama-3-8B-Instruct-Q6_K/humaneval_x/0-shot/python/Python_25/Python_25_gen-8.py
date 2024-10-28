from typing import List

def factorize(n: int) -> List[int]:
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
    # Note: This function does not handle the case where n is a prime number (i.e., only one factor). For example, the output of factorize(7) will be [] instead of [7]. You may want to add a special case for this. If n is prime, the function should return [n].