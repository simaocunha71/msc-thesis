def is_Sum_Of_Powers_Of_Two(n):
    if n <= 0:
        return False
    max_power = 0
    while 2 ** max_power <= n:
        max_power += 1
    for power in range(max_power-1, -1, -1):
        while n >= 2 ** power:
            n -= 2 ** power
    return n == 0