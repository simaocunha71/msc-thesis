"""
def is_Sum_Of_Powers_Of_Two(n):
    if n == 0:
        return False
    while n:
        if not n%2:
            return False
        n = n >> 1
    return True
"""

