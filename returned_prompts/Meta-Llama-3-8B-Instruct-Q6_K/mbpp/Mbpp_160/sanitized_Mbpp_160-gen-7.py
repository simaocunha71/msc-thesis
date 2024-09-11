def find_solution(a, b, n):
    if b == 0:
        if a == 0:
            return None
        return (n, 0)
    x0 = 1
    y0 = 0
    x1 = 0
    y1 = 1
    while b != 0:
        q = a // b
        x = x0 - q * x1
        y = y0 - q * y1
        a, b = b, a % b
        x0, x1 = x1, x
        y0, y1 = y1, y
    if a == 0:
        return None
    return (x0, y0) if n >= 0 else (x0 + n // abs(n) * a, y0 + n // abs(n) * b)  # adjust for negative n