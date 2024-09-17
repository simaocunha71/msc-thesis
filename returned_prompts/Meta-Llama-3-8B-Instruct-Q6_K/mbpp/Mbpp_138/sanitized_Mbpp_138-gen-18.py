def is_Sum_Of_Powers_Of_Two(n):
    powers = []
    i = 0
    while n > 0:
        if n & 1:
            powers.append(2 ** i)
        n >>= 1
        i += 1
    return len(powers) > 0