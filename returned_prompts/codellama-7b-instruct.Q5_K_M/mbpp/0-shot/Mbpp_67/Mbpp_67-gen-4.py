"""
import itertools
def bell_number(n):
    return sum(1 for _ in itertools.combinations_with_replacement(range(n+1), n))
"""
