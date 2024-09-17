def is_Sum_Of_Powers_Of_Two(n):
    if n == 0:
        return False
    while n > 0:
        if n % 2 != 0:
            if n == 1:
                return True
            else:
                return False
        n = n // 2