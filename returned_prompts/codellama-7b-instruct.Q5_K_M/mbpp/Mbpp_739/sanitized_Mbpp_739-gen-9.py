def find_Index(n):
    for i in range(n):
        if (i * (i+1)) // 2 == 10 ** (n-i-1):
            return i
    return -1