def find_solution(a, b, n):
    def extended_gcd(a, b):
        if b == 0:
            return (1, 0)
        x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (x, y)

    x, y = extended_gcd(a, b)
    if a * x + b * y == n:
        return (x, y)
    else:
        return None