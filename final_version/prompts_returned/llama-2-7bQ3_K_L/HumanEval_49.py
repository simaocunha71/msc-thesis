

def modp(n: int, p: int):
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
    return 2**n % p


def test():
    t = int(input())
    for x in range(t):
        n, p = list(map(int, input().split()))
        assert modp(n, p) == 2**n % p == n % (p-1), f"{n}={2**n % p},{p-1}"
        