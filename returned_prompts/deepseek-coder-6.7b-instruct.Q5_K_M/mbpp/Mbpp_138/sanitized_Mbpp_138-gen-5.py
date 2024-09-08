def is_Sum_Of_Powers_Of_Two(n):
    for i in range(n):
        if 2**i == n:
            return True
        if 2**i > n:
            break
    return False