def find_solution(a, b, n):
    if a == 0 and b == 0:
        return None
    if a == 0:
        if n % b == 0:
            return (0, n // b)
        else:
            return None
    if b == 0:
        if n % a == 0:
            return (n // a, 0)
        else:
            return None
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    r, x, y = extended_gcd(a, b)
    if n % r == 0:
        return (x * (n // r), y * (n // r))
    else:
        return None

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

print(find_solution(2, 3, 7))  # => (2, 1)
"""

