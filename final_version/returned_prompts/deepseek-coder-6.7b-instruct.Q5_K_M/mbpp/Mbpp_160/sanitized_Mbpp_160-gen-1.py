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
    if abs(a) > abs(b):
        x = n // a
        y = (n - a * x) // b
        if a * x + b * y == n:
            return (x, y)
        else:
            return None
    else:
        y = n // b
        x = (n - b * y) // a
        if a * x + b * y == n:
            return (x, y)
        else:
            return None