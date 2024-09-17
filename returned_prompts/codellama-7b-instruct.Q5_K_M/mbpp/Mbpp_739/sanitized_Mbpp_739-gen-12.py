def find_Index(n):
    for i in range(1, n):
        i += 1
        n += 1
        if len(str(i * (i + 1) // 2)) == n:
            return i