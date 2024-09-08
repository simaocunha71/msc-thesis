def find_solution(a, b, n):
    if a == 0 and b == 0:
        return None
    if a == 0:
        return (0, n // b) if n % b == 0 else None
    if b == 0:
        return (n // a, 0) if n % a == 0 else None
    r, x, y = extended_gcd(a, b)
    if n % r != 0:
        return None
    return (x * (n // r), y * (n // r))
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x, y = extended_gcd(b % a, a)
    return gcd, y - (b // a) * x, x