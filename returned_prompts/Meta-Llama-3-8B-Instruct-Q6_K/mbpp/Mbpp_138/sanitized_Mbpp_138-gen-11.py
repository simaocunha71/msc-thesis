def is_Sum_Of_Powers_Of_Two(n):
    if n <= 0:
        return False
    powers = [2**i for i in range(n.bit_length(), -1, -1)]
    for p in powers:
        while n >= p:
            n -= p
            if n == 0:
                return True
    return False