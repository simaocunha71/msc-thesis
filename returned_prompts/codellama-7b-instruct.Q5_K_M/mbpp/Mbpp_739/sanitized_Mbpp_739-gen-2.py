def find_Index(n):
    for i in range(1, 10**n):
        num = i * (i+1) // 2
        if len(str(num)) == n:
            return i
    return -1