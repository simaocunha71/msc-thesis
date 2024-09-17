def is_Sum_Of_Powers_Of_Two(n):
    if n == 0:
        return True

    powers = [2**i for i in range(20)]
    for power in powers:
        while power <= n:
            if power == n:
                return True
            power *= 2
    return False