def is_Sum_Of_Powers_Of_Two(n):
    while n > 0:
        if n % 2 == 0:
            n = n // 2
        else:
            return False
    return True