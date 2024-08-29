
def median_trapezium(a, b, c):
    s = (a + b + c) / 2
    return (2 * (s**2 - (a**2 + b**2 + c**2) / 4)**0.5) / 2

assert median_trapezium(15,25,35)==20
"""
"""

