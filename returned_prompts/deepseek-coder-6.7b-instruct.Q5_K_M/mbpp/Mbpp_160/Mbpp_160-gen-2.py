
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
    r, x, y = 0, 0, 0
    if a > b:
        a, b, n = b, a, n
    while a > 0:
        q = n // a
        r = n - q * a
        x = x + q * x
        y = y + q * y
        n, a, x, y = a, r, y, x
    return (n, y) if n == 1 else None


