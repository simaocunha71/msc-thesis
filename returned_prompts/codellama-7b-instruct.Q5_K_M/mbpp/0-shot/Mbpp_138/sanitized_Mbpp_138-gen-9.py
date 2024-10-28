def is_Sum_Of_Powers_Of_Two(n):
    if n == 1:
        return True
    i = 1
    while i <= n:
        if n & (1 << i):
            if is_Sum_Of_Powers_Of_Two(n - (1 << i)):
                return True
        i += 1
    return False