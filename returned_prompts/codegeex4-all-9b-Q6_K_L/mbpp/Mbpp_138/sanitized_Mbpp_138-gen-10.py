def is_Sum_Of_Powers_Of_Two(n):
    while n > 0:
        if n % 2 == 1:
            n -= 1
        else:
            n //= 2
    return n == 0