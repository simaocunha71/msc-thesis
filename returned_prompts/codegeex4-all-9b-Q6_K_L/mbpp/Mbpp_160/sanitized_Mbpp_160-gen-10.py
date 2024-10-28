def find_solution(a, b, n):
    def extended_euclid(a, b):
        if b == 0:
            return (a, 1, 0)
        else:
            d, x, y = extended_euclid(b, a % b)
            return (d, y, x - (a // b) * y)

    d, x, y = extended_euclid(a, b)
    if n % d != 0:
        return None
    else:
        return (x * (n // d), y * (n // d))