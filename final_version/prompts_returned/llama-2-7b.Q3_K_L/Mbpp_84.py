"""
Write a function to find the nth number in the newman conway sequence.
assert sequence(10) == 6
"""
def sequence(n):
    return sum([int(k**0.5) for k in range(-1, n-1,-1)]+[1])
