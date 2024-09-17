def sequence(n):
    num = 1
    for _ in range(n - 1):
        num += len(str(num))
    return num