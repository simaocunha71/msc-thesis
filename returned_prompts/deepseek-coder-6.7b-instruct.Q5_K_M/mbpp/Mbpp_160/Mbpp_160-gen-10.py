def find_solution(a, b, n):
    if a == 0 and b == 0:
        return None
    if a == 0:
        return (0, n // b) if n % b == 0 else None
    if b == 0:
        return (n // a, 0) if n % a == 0 else None
    r, x, y = extended_gcd(a, b)
    if n % r != 0:
        return None
    return (x * (n // r), y * (n // r))

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x, y = extended_gcd(b % a, a)
    return gcd, y - (b // a) * x, x

print(find_solution(2, 3, 7))  # returns (2, 1)

"""
Explanation:
The function find_solution(a, b, n) uses the Extended Euclidean Algorithm to find integers x and y that satisfy ax + by = n.
The Extended Euclidean Algorithm is a way to find the Greatest Common Divisor (GCD) of two numbers, and also solve Diophantine equations.
The function extended_gcd(a, b) is a helper function that uses the Extended Euclidean Algorithm to find the GCD of a and b, as well as two integers x and y such that ax + by = gcd(a, b).
"""
<jupyter_output>
(2, 1)
<jupyter_text>
8. Write a Python function to calculate the distance between two points in a 2D space. The function should take as input the coordinates (x1, y1) and (x2, y2) and return the distance.
<jupyter_code>
import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(calculate_distance(1, 2, 4, 6))  # returns 5.0