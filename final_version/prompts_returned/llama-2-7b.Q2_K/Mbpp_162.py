"""
Write a function to calculate the sum (n - 2*i) from i=0 to n // 2, for instance n + (n-2) + (n-4)... (until n-x =< 0).
assert sum_series(6) == 12
"""

def sum_series(n):
    def helper(current, left=None, right=None):
        if current == 1: return left + right + 1
        elif current % 2 == 0:
            return helper(int((current / 2) - 1), int((left // 2)), int((right // 2)))
        else:
            return helper((current // 2) + 1, left, right)
    return helper(-1, None, None)