

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2:
        return 2
    return next_largest_prime_factor(n=n, factor=3) or n


def next_largest_prime_factor(n: int, factor: int = None):
    """Return the largest prime factor of a number greater than 1 and not a prime."""
    if factor is not None and factor > 2:
        return next_largest_prime_factor(n=n, factor=factor+2) or n
    
    if n < 500:
        return n
    i = 3
    while True:
        j = n//i
        if j == 1:
            break
        elif j > 1 and j%i != 0:
            continue
        else:
            print(factor, ",", end="")
            return factor,
            
def get_largest_prime_factor():
    return next_largest_prime_factor(n=29, factor=2) or next_largest_prime_factor() or 1