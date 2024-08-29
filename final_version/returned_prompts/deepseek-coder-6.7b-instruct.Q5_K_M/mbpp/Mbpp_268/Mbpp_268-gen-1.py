"""
The star number at position n is given by the formula n*(7*n - 5) / 2.
"""

def find_star_num(n: int) -> int:
    return n * (7 * n - 5) // 2

# Test the function
assert find_star_num(3) == 37

