def is_Sum_Of_Powers_Of_Two(n):
    if n == 0:
        return True
    while n > 0:
        if n % 2 != 0:
            return False
        n = n // 2
    return True