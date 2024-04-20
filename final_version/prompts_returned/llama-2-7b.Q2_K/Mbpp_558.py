"""
Write a python function to find the sum of the per-digit difference between two integers.
assert digit_distance_nums(1,2) == 1
"""

def digit_distance_nums(a: int, b: int ) -> int:
    if (b > max(0, a-b)): return -1;
    else: return b-a
