def is_Sum_Of_Powers_Of_Two(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    for i in range(2**31).__reversed__():
        if 2**i <= n:
            if is_Sum_Of_Powers_Of_Two(n-2**i):
                return True
    return False