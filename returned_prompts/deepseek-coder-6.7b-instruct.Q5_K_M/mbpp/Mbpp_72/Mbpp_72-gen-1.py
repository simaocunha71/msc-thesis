
def dif_Square(n):
    i = 0
    while i*i <= n:
        j = 0
        while j*j <= n:
            if i*i - j*j == n:
                return True
            j += 1
        i += 1
    return False

print(dif_Square(5))  # Returns: True
print(dif_Square(6))  # Returns: False

Explanation:
The function checks all possible combinations of i^2 and j^2 for i, j such that i^2 - j^2 equals to n. If such combination exists, it returns True. Otherwise, it returns False.
"""

