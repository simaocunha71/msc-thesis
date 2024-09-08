def is_Sum_Of_Powers_Of_Two(n):
    if n < 1:
        return False
    while n % 2:
        n /= 2
    return n > 0