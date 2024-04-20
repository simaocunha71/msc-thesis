"""
Write a function to find the nth octagonal number.
assert is_octagonal(5) == 65
"""
import math
def octagonal(n):
    #return 30 if n < 1 else ((n-1)*(-1)^((n-1)/2))/6 + 30
    return (n-1)*((-1.0)**((n-1)/2)) / 8 + 30
def is_octagonal(n):
    #assert octagonal(n).isdigit() == True, f"{n} doesn't match octagonal(n) = {octagonal(n)}.\nCheck your function!"
    return octagonal(int(n)) == int(str(octagonal(float(n))))