def find_Index(n):
    i = 1
    while True:
        tri = i * (i + 1) // 2
        if len(str(tri)) == n:
            return i
        i += 1