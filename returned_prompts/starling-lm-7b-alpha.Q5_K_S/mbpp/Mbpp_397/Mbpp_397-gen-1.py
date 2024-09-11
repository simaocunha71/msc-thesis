"""
def median_numbers(a,b,c):
    if a<b<c:
        return b
    if a<c<b:
        return c
    if b<a<c:
        return a
    if b<c<a:
        return c
    if c<a<b:
        return a
    if c<b<a:
        return b
"""

from statistics import median
def median_numbers(a,b,c):
    return median([a,b,c])

assert median_numbers(25,55,65)==55.0


