def is_Sum_Of_Powers_Of_Two(n):
    if n <= 0:
        return False
    powers = 0
    while 2**powers <= n:
        if 2**powers == n:
            return True
        n -= 2**powers
        powers += 1
    return False