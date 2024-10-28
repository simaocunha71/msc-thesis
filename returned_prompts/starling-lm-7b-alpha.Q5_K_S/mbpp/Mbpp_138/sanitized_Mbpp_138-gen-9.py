def is_Sum_Of_Powers_Of_Two(n):
    while n != 0:
        if n % 2 == 1:
            return False
        else:
            n = n >> 1
    return True