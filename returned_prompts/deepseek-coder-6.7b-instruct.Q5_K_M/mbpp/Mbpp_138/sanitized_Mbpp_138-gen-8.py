def is_Sum_Of_Powers_Of_Two(n):
    if n < 1:
        return False
    if n == 1 or n == 2:
        return True
    while n > 1:
        power = 0
        while 2**power <= n:
            if 2**power == n:
                return True
            power += 1
        n -= 1
    return False