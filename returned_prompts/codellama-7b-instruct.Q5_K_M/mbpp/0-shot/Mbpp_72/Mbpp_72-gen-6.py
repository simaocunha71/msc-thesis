"""
# Iterate from the square root of the given number towards 0
# Check if the number can be expressed as the sum of two squares
# If yes, return True
# Else, return False

def dif_Square(n):
    for i in range(int(n**0.5), 0, -1):
        j = (n - i)**0.5
        if (i == j) or (i + j)**2 == n:
            return True
    return False

"""

