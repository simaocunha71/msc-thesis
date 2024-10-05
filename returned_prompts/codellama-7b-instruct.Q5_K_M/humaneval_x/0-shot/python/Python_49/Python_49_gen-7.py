

def modp(n: int, p: int) -> int:
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    if n < 0:
        n = 2 ** -n
    return pow(2, n, p)

# 1101 -> 2^3 mod 101 -> 2^3 % 101 -> 8
# 0 -> 2^0 mod 101 -> 1
# 100 -> 2^6 mod 101 -> 1

