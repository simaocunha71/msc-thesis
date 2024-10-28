from fractions import gcd
def find_solution(a, b, n):
    g = gcd(a, b)
    if n % g != 0:
        return None
    k = n / g
    b, a = a, b
    if a < 0:
        k = -k
        a, b = -a, -b
    if b < 0:
        k = -k
        b = -b
    if a > 0:
        k = -k
        a = -a
    return (k * b, -k * a)