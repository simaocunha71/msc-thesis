def is_Sum_Of_Powers_Of_Two(n):
    while n:
        if (n & 1):
            if n == 1:
                return True
            else:
                return False
        n >>= 1
    return True