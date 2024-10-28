def is_Sum_Of_Powers_Of_Two(n):
    if n < 1:
        return False
    powers = []
    i = 0
    while (1 << i) <= n:
        powers.append(1 << i)
        i += 1
    for power in powers:
        if n == power:
            return True
        while power <= n:
            n -= power
            if n == 0:
                return True
    return False