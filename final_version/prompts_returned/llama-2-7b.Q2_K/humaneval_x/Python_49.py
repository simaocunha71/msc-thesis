

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

def modsqrt(b: int, n: int):
    assert b >= 0, "Negative number"
    if n == 0 or b < 0:
        raise ZeroDivisionError("Can't sqrt on zero")
    c = modp(modp(n, 2), modp(b, 3)) + n % (b + 1)
    return modsqrt(c, n - c)

def modsqrt(a: int, b: int):
    assert a >= 0, "Negative number"
    if b < 0 or a == 0:
        raise ZeroDivisionError("Can't sqrt on zero")
    return (modp(b + 1, 3) - modp(a, 2)) / n % modp(b, 3)

def modpow(a, b, m):
    assert a >= 0 and b >= 0, "Negative numbers"
    result = 1
    while m > 0:
        remainder = m & b
        if remainder == 0: break
        new_power = remainder | (m // 2)
        a /= 2
        result *= a
    return result

def main():
    print("modp(3, 5):\t", modp(3, 5), "\n")
    print("modp(1101, 101):\t", modp(1101, 101))
    print("modp(0, 101):\t", modp(0, 101))
    print("modp(