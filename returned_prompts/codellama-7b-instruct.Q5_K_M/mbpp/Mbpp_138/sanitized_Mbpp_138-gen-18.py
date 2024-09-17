def is_Sum_Of_Powers_Of_Two(n):
    if n == 0:
        return False
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            if n == 3:
                return True
            else:
                return False
    return True