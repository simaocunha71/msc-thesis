def find_solution(a, b, n):
    if a == 0:
        if b == 0:
            return None
        else:
            return None
    if b == 0:
        return n // a, 0
    d = gcd(a, b)
    a //= d
    b //= d
    if n % d != 0:
        return None
    n //= d
    x0 = 1
    y0 = 0
    x1 = 0
    y1 = 1
    while n > 0:
        q = n // a
        t = a
        a = b % t
        b = t
        n = n % t
        x = x1 - q * x0
        y = y1 - q * y0
        x0 = x1
        x1 = x
        y0 = y1
        y1 = y
    if b > 0:
        return None
    return x0, y0
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)