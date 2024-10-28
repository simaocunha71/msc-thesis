def is_Sum_Of_Powers_Of_Two(n):
    if n == 0:
        return False
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            return False
    return True
