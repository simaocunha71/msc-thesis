def find_solution(a, b, n):
    if a == 0 and b == 0:
        return None
    if n == 0:
        return (0, 0)
    if a == 0:
        if n % b != 0:
            return None
        return (0, n // b)
    if b == 0:
        if n % a != 0:
            return None
        return (n // a, 0)
    if a > 0 and b > 0:
        gcd = find_gcd(a, b)
        if n % gcd != 0:
            return None
        x = n // gcd * (b // gcd)
        y = -(a // gcd * (n // gcd))
        return (x, y)
    if a < 0 and b > 0:
        gcd = find_gcd(-a, b)
        if n % gcd != 0:
            return None
        x = (n // gcd * (b // gcd)) - (a // gcd * (n // gcd))
        y = -(a // gcd * (n // gcd))
        return (x, y)
    if a > 0 and b < 0:
        gcd = find_gcd(a, -b)
        if n % gcd != 0:
            return None
        x = n // gcd * (b // gcd)
        y = (a // gcd * (n // gcd)) + (b // gcd * (n // gcd))
        return (x, y)
    if a < 0 and b < 0:
        gcd = find_gcd(-a, -b)
        if n % gcd != 0:
            return None
        x = (n // gcd * (b // gcd)) - (a // gcd * (n // gcd))
        y = (a // gcd * (n // gcd)) + (b // gcd * (n // gcd))
        return (x, y)
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a