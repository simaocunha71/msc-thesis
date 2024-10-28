def is_Sum_Of_Powers_Of_Two(n):
    while n > 0:
        if n & (n - 1) == 0:
            return True
        n &= n - 1
    return False