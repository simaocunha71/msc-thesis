
def climb_stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climb_stairs(n - 1) + climb_stairs(n - 2)

"""
Write a function that returns the number of ways to climb n stairs.
"""

