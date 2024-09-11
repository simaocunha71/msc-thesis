from sympy import gcd
def find_solution(a, b, n):
    if gcd(a, b) != 1:
        return None
    x0 = n // a
    y0 = (n % a) // b
    x = x0
    y = y0
    while x0 * a + y0 * b != n:
        x0, y0 = y0, x0 - (n - x0 * a) // b
    return (x0, y0)  # return x and y as a tuple