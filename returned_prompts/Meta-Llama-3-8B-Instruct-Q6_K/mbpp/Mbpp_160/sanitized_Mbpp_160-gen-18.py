def find_solution(a, b, n):
    if a == 0 and b == 0:
        return None
    if gcd(a, b) != 1:
        return None
    x0, y0 = extended_euclidean(a, b)
    if n % b == 0:
        x = n // b * y0
        y = -n // b * x0
    else:
        x = n // b * y0 + x0
        y = n % b
    return x, y
def extended_euclidean(a, b):
    if b == 0:
        return 1, 0
    x, y = extended_euclidean(b, a % b)
    return y, x - y * (a // b)