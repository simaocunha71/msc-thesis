from fractions import gcd
def find_solution(a, b, n):
    g = gcd(a, b)
    if n % g != 0:
        return None
    x, y = (n * b // g + a * b) // g, (n * a // g - b * a) // g
    return (x, y)