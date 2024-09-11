"""
from math import log,pow
def is_Sum_Of_Powers_Of_Two(n):
    while n % 2 == 0:
        n = n / 2
    if n == 1:
        return True
    return False

print(is_Sum_Of_Powers_Of_Two(10))
"""

