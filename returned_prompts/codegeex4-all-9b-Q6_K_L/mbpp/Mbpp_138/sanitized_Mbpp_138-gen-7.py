def is_Sum_Of_Powers_Of_Two(n):
    while n > 0:
        if n % 2 != 0 and n != 1:
            return False
        n = n // 2
    return True