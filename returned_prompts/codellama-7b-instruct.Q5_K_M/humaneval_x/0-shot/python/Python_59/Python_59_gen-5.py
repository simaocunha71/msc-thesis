
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.
    """
    if n == 1:
        return 1
    if is_prime(n):
        return n
    for i in range(int(sqrt(n)), 1, -1):
        if n % i == 0 and is_prime(i):
            return i
    return 1

def is_prime(n: int) -> bool:
    """
    Return True if n is a prime number, False otherwise.
    """
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
