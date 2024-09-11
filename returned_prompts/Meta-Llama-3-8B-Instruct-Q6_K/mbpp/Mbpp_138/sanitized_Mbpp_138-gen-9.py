def is_Sum_Of_Powers_Of_Two(n):
    if n < 0:
        return False
    for i in range(n.bit_length(), -1, -1):
        if 1 << i <= n:
            n -= 1 << i
    return n == 0