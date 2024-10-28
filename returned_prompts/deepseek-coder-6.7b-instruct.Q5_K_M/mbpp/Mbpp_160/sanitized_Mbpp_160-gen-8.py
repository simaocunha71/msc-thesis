import unittest
from main import find_solution
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

    if a > b:
        q, r = divmod(n, a)
        if r == 0:
            return (0, q)
        x, y = find_solution(b % a, a, r)
        return (x + q * y, y)
    else:
        q, r = divmod(n, b)
        if r == 0:
            return (q, 0)
        x, y = find_solution(a, b % a, r)
        return (x, y + q * y)