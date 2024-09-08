def is_woodall(n):
    num = str(n)
    for i in range(len(num) - 1):
        if num[i] > num[i+1]:
            return False
    return True