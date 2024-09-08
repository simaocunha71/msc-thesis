def dif_Square(n):
    # Check if the number can be represented as the difference of two squares
    for i in range(1, int(n**0.5) + 1):
        if (n + i) % (2 * i) == 0:
            return True
    return False