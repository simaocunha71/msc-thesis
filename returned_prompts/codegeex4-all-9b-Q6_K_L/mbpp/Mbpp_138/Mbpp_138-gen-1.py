def is_Sum_Of_Powers_Of_Two(n):
    if n == 0:
        return True
    if n == 1:
        return False
    count = 0
    while n > 0:
        if n % 2 != 0:
            count += 1
        if count > 1:
            return False
        n = n // 2
    return True